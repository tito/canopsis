#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------
# Copyright (c) 2014 "Capensis" [http://www.capensis.com]
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

from unittest import TestCase, main

from canopsis.middleware import Middleware, SCHEME_SEPARATOR
from canopsis.middleware.manager import Manager

from tempfile import NamedTemporaryFile

from os import remove


class TestUnregisteredMiddleware(Middleware):

    __protocol__ = 'noprototest'


class TestRegisteredMiddleware(Middleware):

    __register__ = True
    __protocol__ = 'prototest'


class TestRegisteredWithDataTypeMiddleware(TestRegisteredMiddleware):

    __datatype__ = 'datatypetest'


class ManagerTest(TestCase):

    def setUp(self):

        self.file_name = NamedTemporaryFile().name
        self.category = 'TEST'

        class TestManager(Manager):
            def _get_conf_paths(_self, *args, **kwargs):
                result = super(TestManager, _self)._get_conf_paths(
                    *args, **kwargs)
                result.append(self.file_name)
                return result

            def _conf(_self, *args, **kwargs):
                result = super(TestManager, _self)._conf(*args, **kwargs)
                result.add_unified_category(self.category)
                return result

        self.manager = TestManager()

    def test_configure(self):

        rwdtm = TestRegisteredWithDataTypeMiddleware()

        middleware = 'test'

        with open(self.file_name, 'w') as _file:
            _file.write('[%s]' % self.category)
            _file.write('\n%s_uri=%s' % (middleware, rwdtm.uri))

        self.manager.apply_configuration()

        self.assertEqual(self.manager[middleware].protocol, rwdtm.protocol)
        self.assertEqual(self.manager[middleware].data_type, rwdtm.data_type)
        self.assertEqual(self.manager[middleware].data_scope, rwdtm.data_scope)

        remove(self.file_name)

    def test_get_middleware(self):

        uri = '%s://' % (TestUnregisteredMiddleware.__protocol__)

        self.assertRaises(
            Middleware.Error, self.manager.get_middleware_by_uri, uri)

        uri = '%s://' % (TestRegisteredMiddleware.__protocol__)

        middleware = self.manager.get_middleware_by_uri(uri)

        self.assertTrue(type(middleware) is TestRegisteredMiddleware)

        middleware2 = self.manager.get_middleware_by_uri(uri)

        self.assertTrue(middleware is middleware2)

        middleware3 = self.manager.get_middleware_by_uri(uri, shared=False)

        self.assertFalse(middleware is middleware3)

        self.manager.shared = False

        middleware4 = self.manager.get_middleware_by_uri(uri)

        self.assertFalse(middleware is middleware4)

        uri = '%s%s%s://' % (
            TestRegisteredWithDataTypeMiddleware.__protocol__,
            SCHEME_SEPARATOR,
            TestRegisteredWithDataTypeMiddleware.__datatype__)

        middleware_wd = self.manager.get_middleware_by_uri(uri)

        self.assertTrue(
            type(middleware_wd) is TestRegisteredWithDataTypeMiddleware)

if __name__ == '__main__':
    main()