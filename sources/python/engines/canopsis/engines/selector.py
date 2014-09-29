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

from canopsis.engines import Engine
from canopsis.old.storage import get_storage
from canopsis.old.account import Account
from canopsis.old.selector import Selector
import time


class engine(Engine):
    """
        This engine's goal is to compute an aggregated information from an event selection.
        The event selection is done thanks to a filter whitch can include event, exclude events or select them from a cfilter.
        The worst state is then computed on the selected event set and a new event holding this information is produced.
        This computation is triggered each time the crecord dispatcher emit a crecord event of selector type.
    """

    etype = 'selector'

    def __init__(self, *args, **kargs):
        super(engine, self).__init__(*args, **kargs)

        self.selectors = []
        self.nb_beat = 0
        self.thd_warn_sec_per_evt = 1.5
        self.thd_crit_sec_per_evt = 2

    def pre_run(self):
        #load selectors
        self.storage = get_storage(
            namespace='object', account=Account(user="root", group="root"))

    def beat(self):
        self.logger.debug('entered in selector BEAT')

    def consume_dispatcher(self, event, *args, **kargs):
        self.logger.debug('entered in selector consume dispatcher')
        # Gets crecord from amqp distribution

        selector = self.get_ready_record(event)

        if selector:

            event_id = event['_id']

            # Loads associated class
            selector = Selector(
                storage=self.storage, record=selector,
                logging_level=self.logging_level)

            name = selector.display_name

            self.logger.debug('Selector {} found, start processing..'.format(
                name
            ))

            # do I publish a selector event ? Yes if selector have to
            # and it is time or we got to update status
            if selector.dostate:
                self.publish_event(selector)
            else:
                self.logger.debug('Nothing to do with selector {}'.format(
                    name
                ))

            #Update crecords informations
            self.crecord_task_complete(event_id)

        self.nb_beat += 1
        #set record free for dispatcher engine

    def publish_event(self, selector):

        rk, selector_event, publish_ack = selector.event()
        selector_event['selector_id'] = selector._id

        self.logger.info(
            'Ready to publish selector {} event with state {}'.format(
                selector.display_name,
                selector_event['state']
            )
        )

        if publish_ack:
            #define a clean ack information to the event
            now = int(time.time())
            selector_event['ack'] = {
                'timestamp': now,
                'rk': rk,
                'author': 'canopsis',
                'comment': 'All matched event are acknowleged',
                'isAck': True
            }
            self.logger.debug(' + Selector event is ack because all matched event are ack')
        else:
            #define or reset ack key for selector generated event
            selector_event['ack'] = {}
            self.logger.debug(' + Selector event is NOT ack')

        # Publish Sla information when available
        if selector.sla_rk:
            selector_event['sla_rk'] = selector.sla_rk

        self.amqp.publish(
            selector_event,
            rk,
            self.amqp.exchange_name_events
        )

        self.logger.debug("published event selector {}".format(
            selector.display_name
        ))