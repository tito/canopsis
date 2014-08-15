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

from unittest import main

from test.manager.file import ConfigurationManagerTest

from canopsis.configuration.manager.file.json import JSONConfigurationManager


class ConfigurationManagerTest(ConfigurationManagerTest):

    def _get_configuration_manager(self):

        return JSONConfigurationManager()

    def _get_manager_path(self):

        return 'canopsis.configuration.manager.file.json.JSONConfigurationManager'

    def _get_manager(self):

        return JSONConfigurationManager

if __name__ == '__main__':
    main()
