# -*- coding: utf-8 -*-
#--------------------------------
# Copyright (c) 2011 "Capensis" [http://www.capensis.com]
#
# This file is part of Canopsis.
#
# Canopsis is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Canopsis is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Canopsis.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------

from canopsis.topology.manager import Topology
from canopsis.context.manager import Context

from time import time

context = Context()
topology = Topology()


def event_processing(event, ctx=None, **params):
    """
    Process input event in getting topology nodes bound to input event entity.

    One topology nodes are founded, executing related rules.
    """
    if ctx is None:
        ctx = {}

    entity = context.get_entity(event=event)

    # do something only if state is different than previous one
    if entity['state'] != event['state']:

        entity_id = context.get_entity_id(entity)

        nodes = topology.get_nodes(entity_id=entity_id)

        for node in nodes:

            next_nodes = topology.get_next_nodes(node)

            for next_node in next_nodes:

                ctx['source_node'] = node
                ctx['node'] = next_node
                rule = next_node['rule']

                process_rule(event=event, rule=rule, ctx=ctx)

    return event


class engine(Engine):
    etype = 'topology2'

    def __init__(self, *args, **kargs):
        super(engine, self).__init__(*args, **kargs)

        # load topology manager
        self.topology = Topology()
        self.context = Context()

    def work(self, event, *args, **kwargs):

        # get nodes related to event if exist
        if 'id' not in event:
            event['id'] = event[event['source_type']]

        entity_id = self.context.get_entity_id(event)
        nodes = self.topology.find_nodes_by_entity_id(entity_id=entity_id)

        # for all node, apply rule if exist
        for node in nodes:
            rule = node.get('rule')

            # if a rule exist, apply it and update node
            if rule is not None:
                # apply it
                apply_rule = getattr(self, rule)
                node['entity'] = event
                node = apply_rule(self, node, **rule)

            # if state has changed
            if node['state'] != event['state']:
                # update the node
                self.topology.push_node(_id=node['name'], node=node)

                # and publish the change of state to all next nodes
                next = nodes.get('next')
                if next is not None:
                    for n in next:
                        n_id = self.context.get_entity_id(n)
                        topology_propagation = {
                            'connector': 'engine',
                            'connector_name': self.etype,
                            'event_type': "topology-propagation",
                            "source_type": "topology-node",
                            'entity_id': n_id,
                            'topology-node': n['name'],
                            "name": n['name'],
                            "node": node,
                            'timestamp': time(),
                            'state': node['state']
                        }
                self.amqp.publish(
                    msg=topology_propagation, routing_key='',
                    exchange_name=self.amqp.exchange_name_events)

        return event


def operation(
    event, ctx, at_least, at_most, check_state, in_state, default_state=0,
    **kwargs
):
    """
    Do a generic state operation
    """

    node = ctx['node']

    result = node

    state = node['state']

    # do something only if check_state is different than state
    if state != check_state:
        entity_id = context.get_entity_id(node)
        source_nodes = topology.find_nodes_by_next(next=entity_id)
        len_source_nodes = len(source_nodes)
        for source_node in source_nodes:
            at_most = len_source_nodes - at_most
            if check_state == source_node['state']:
                at_least -= 1
                at_most -= 1
            if at_least <= 0 or at_most <= 0:
                result['state'] = in_state
                break

        if result['state'] != in_state:
            result['state'] = default_state

    return result


def all(event, ctx, check_state, in_state, default_state):
    """
    Check if all source nodes match with input check_state
    """

    node = ctx['node']

    node_id = context.get_entity_id(node)
    source_nodes = topology.find_nodes_by_next(next=node_id)
    len_source_nodes = len(source_nodes)

    return operation(
        node, at_least=len_source_nodes, at_most=len_source_nodes,
        check_state=check_state, default_state=default_state,
        in_state=in_state)


def any(event, ctx, check_state, in_state, default_state):
    """
    Check if all source nodes match with input check_state
    """

    node = ctx['node']

    node_id = context.get_entity_id(node)
    source_nodes = topology.find_nodes_by_next(next=node_id)
    len_source_nodes = len(source_nodes)

    return operation(
        node, at_least=1, at_most=len_source_nodes,
        check_state=check_state, default_state=default_state,
        in_state=in_state)


def worst_state(event, ctx):
    """
    Check the worst state among source nodes.
    """

    node = ctx['node']

    result = node

    entity = node['entity']
    entity_id = context.get_entity_id(node)

    if entity['state'] >= node['state']:
        result['state'] = entity['state']

    else:
        source_nodes = topology.find_nodes_by_next(next=entity_id)
        result['state'] = max(
            source_node['state'] for source_node in source_nodes)

    return result


def best_state(event, ctx):
    """
    Get the best state among source nodes.
    """

    node = ctx['node']

    result = node

    entity = node['entity']
    entity_id = context.get_entity_id(node)

    if entity['state'] <= node['state']:
        result['state'] = entity['state']

    else:
        source_nodes = topology.find_nodes_by_next(next=entity_id)
        result['state'] = min(
            source_node['state'] for source_node in source_nodes)

    return result