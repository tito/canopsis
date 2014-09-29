notifications_oid = {'1.3.6.1.4.1.674.10892.1.0.1001': 'alertSystemUp',
 '1.3.6.1.4.1.674.10892.1.0.1004': 'alertThermalShutdown',
 '1.3.6.1.4.1.674.10892.1.0.1006': 'alertAutomaticSystemRecovery',
 '1.3.6.1.4.1.674.10892.1.0.1007': 'alertUserHostSystemReset',
 '1.3.6.1.4.1.674.10892.1.0.1013': 'alertSystemPeakPowerNewPeak',
 '1.3.6.1.4.1.674.10892.1.0.1014': 'alertSystemSoftwareEvent',
 '1.3.6.1.4.1.674.10892.1.0.1052': 'alertTemperatureProbeNormal',
 '1.3.6.1.4.1.674.10892.1.0.1053': 'alertTemperatureProbeWarning',
 '1.3.6.1.4.1.674.10892.1.0.1054': 'alertTemperatureProbeFailure',
 '1.3.6.1.4.1.674.10892.1.0.1055': 'alertTemperatureProbeNonRecoverable',
 '1.3.6.1.4.1.674.10892.1.0.1102': 'alertCoolingDeviceNormal',
 '1.3.6.1.4.1.674.10892.1.0.1103': 'alertCoolingDeviceWarning',
 '1.3.6.1.4.1.674.10892.1.0.1104': 'alertCoolingDeviceFailure',
 '1.3.6.1.4.1.674.10892.1.0.1105': 'alertCoolingDeviceNonRecoverable',
 '1.3.6.1.4.1.674.10892.1.0.1152': 'alertVoltageProbeNormal',
 '1.3.6.1.4.1.674.10892.1.0.1153': 'alertVoltageProbeWarning',
 '1.3.6.1.4.1.674.10892.1.0.1154': 'alertVoltageProbeFailure',
 '1.3.6.1.4.1.674.10892.1.0.1155': 'alertVoltageProbeNonRecoverable',
 '1.3.6.1.4.1.674.10892.1.0.1202': 'alertAmperageProbeNormal',
 '1.3.6.1.4.1.674.10892.1.0.1203': 'alertAmperageProbeWarning',
 '1.3.6.1.4.1.674.10892.1.0.1204': 'alertAmperageProbeFailure',
 '1.3.6.1.4.1.674.10892.1.0.1205': 'alertAmperageProbeNonRecoverable',
 '1.3.6.1.4.1.674.10892.1.0.1252': 'alertChassisIntrusionNormal',
 '1.3.6.1.4.1.674.10892.1.0.1254': 'alertChassisIntrusionDetected',
 '1.3.6.1.4.1.674.10892.1.0.1304': 'alertRedundancyNormal',
 '1.3.6.1.4.1.674.10892.1.0.1305': 'alertRedundancyDegraded',
 '1.3.6.1.4.1.674.10892.1.0.1306': 'alertRedundancyLost',
 '1.3.6.1.4.1.674.10892.1.0.1352': 'alertPowerSupplyNormal',
 '1.3.6.1.4.1.674.10892.1.0.1353': 'alertPowerSupplyWarning',
 '1.3.6.1.4.1.674.10892.1.0.1354': 'alertPowerSupplyFailure',
 '1.3.6.1.4.1.674.10892.1.0.1403': 'alertMemoryDeviceWarning',
 '1.3.6.1.4.1.674.10892.1.0.1404': 'alertMemoryDeviceFailure',
 '1.3.6.1.4.1.674.10892.1.0.1405': 'alertMemoryDeviceNonRecoverable',
 '1.3.6.1.4.1.674.10892.1.0.1452': 'alertFanEnclosureInsertion',
 '1.3.6.1.4.1.674.10892.1.0.1453': 'alertFanEnclosureRemoval',
 '1.3.6.1.4.1.674.10892.1.0.1454': 'alertFanEnclosureExtendedRemoval',
 '1.3.6.1.4.1.674.10892.1.0.1501': 'alertACPowerCordNoPowerNonRedundant',
 '1.3.6.1.4.1.674.10892.1.0.1502': 'alertACPowerCordNormal',
 '1.3.6.1.4.1.674.10892.1.0.1504': 'alertACPowerCordFailure',
 '1.3.6.1.4.1.674.10892.1.0.1552': 'alertLogNormal',
 '1.3.6.1.4.1.674.10892.1.0.1553': 'alertLogWarning',
 '1.3.6.1.4.1.674.10892.1.0.1554': 'alertLogFull',
 '1.3.6.1.4.1.674.10892.1.0.1602': 'alertProcessorDeviceStatusNormal',
 '1.3.6.1.4.1.674.10892.1.0.1603': 'alertProcessorDeviceStatusWarning',
 '1.3.6.1.4.1.674.10892.1.0.1604': 'alertProcessorDeviceStatusFailure',
 '1.3.6.1.4.1.674.10892.1.0.1651': 'alertDeviceAdd',
 '1.3.6.1.4.1.674.10892.1.0.1652': 'alertDeviceRemove',
 '1.3.6.1.4.1.674.10892.1.0.1653': 'alertDeviceConfigError',
 '1.3.6.1.4.1.674.10892.1.0.1702': 'alertBatteryNormal',
 '1.3.6.1.4.1.674.10892.1.0.1703': 'alertBatteryWarning',
 '1.3.6.1.4.1.674.10892.1.0.1704': 'alertBatteryFailure',
 '1.3.6.1.4.1.674.10892.1.0.1754': 'alertSDCardDeviceFailure'}
notifications = {'alertACPowerCordFailure': {'ARGUMENTS': '{2}',
                             'SEVERITY': 'CRITICAL',
                             'STATE': 'DEGRADED',
                             'SUMMARY': '%s',
                             'TIMEINDEX': '99',
                             'TYPE': 'Server AC Cord Failure'},
 'alertACPowerCordNoPowerNonRedundant': {'ARGUMENTS': '{2}',
                                         'SEVERITY': 'INFORMATIONAL',
                                         'STATE': 'OPERATIONAL',
                                         'SUMMARY': '%s',
                                         'TIMEINDEX': '99',
                                         'TYPE': 'Server AC Cord No Power Non'},
 'alertACPowerCordNormal': {'ARGUMENTS': '{2}',
                            'SEVERITY': 'INFORMATIONAL',
                            'STATE': 'OPERATIONAL',
                            'SUMMARY': '%s',
                            'TIMEINDEX': '99',
                            'TYPE': 'Server AC Cord Normal'},
 'alertAmperageProbeFailure': {'ARGUMENTS': '{2}',
                               'SEVERITY': 'CRITICAL',
                               'STATE': 'DEGRADED',
                               'SUMMARY': '%s',
                               'TIMEINDEX': '99',
                               'TYPE': 'Server Amperage Failure'},
 'alertAmperageProbeNonRecoverable': {'ARGUMENTS': '{2}',
                                      'SEVERITY': 'CRITICAL',
                                      'STATE': 'DEGRADED',
                                      'SUMMARY': '%s',
                                      'TIMEINDEX': '99',
                                      'TYPE': 'Server Amperage Nonrecoverable'},
 'alertAmperageProbeNormal': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'INFORMATIONAL',
                              'STATE': 'OPERATIONAL',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Amperage Normal'},
 'alertAmperageProbeWarning': {'ARGUMENTS': '{2}',
                               'SEVERITY': 'MINOR',
                               'STATE': 'DEGRADED',
                               'SUMMARY': '%s',
                               'TIMEINDEX': '99',
                               'TYPE': 'Server Amperage Warning'},
 'alertAutomaticSystemRecovery': {'ARGUMENTS': '{2}',
                                  'SEVERITY': 'CRITICAL',
                                  'STATE': 'OPERATIONAL',
                                  'SUMMARY': '%s',
                                  'TIMEINDEX': '99',
                                  'TYPE': 'Server Automatic System Recovery'},
 'alertBatteryFailure': {'ARGUMENTS': '{2}',
                         'SEVERITY': 'CRITICAL',
                         'STATE': 'DEGRADED',
                         'SUMMARY': '%s',
                         'TIMEINDEX': '99',
                         'TYPE': 'Server Battery Failure'},
 'alertBatteryNormal': {'ARGUMENTS': '{2}',
                        'SEVERITY': 'INFORMATIONAL',
                        'STATE': 'OPERATIONAL',
                        'SUMMARY': '%s',
                        'TIMEINDEX': '99',
                        'TYPE': 'Server Battery Normal'},
 'alertBatteryWarning': {'ARGUMENTS': '{2}',
                         'SEVERITY': 'MINOR',
                         'STATE': 'DEGRADED',
                         'SUMMARY': '%s',
                         'TIMEINDEX': '99',
                         'TYPE': 'Server Battery Warning'},
 'alertChassisIntrusionDetected': {'ARGUMENTS': '{2}',
                                   'SEVERITY': 'CRITICAL',
                                   'STATE': 'OPERATIONAL',
                                   'SUMMARY': '%s',
                                   'TIMEINDEX': '99',
                                   'TYPE': 'Server Chassis Intrusion Detected'},
 'alertChassisIntrusionNormal': {'ARGUMENTS': '{2}',
                                 'SEVERITY': 'INFORMATIONAL',
                                 'STATE': 'OPERATIONAL',
                                 'SUMMARY': '%s',
                                 'TIMEINDEX': '99',
                                 'TYPE': 'Server Chassis Intrusion Normal'},
 'alertCoolingDeviceFailure': {'ARGUMENTS': '{2}',
                               'SEVERITY': 'CRITICAL',
                               'STATE': 'DEGRADED',
                               'SUMMARY': '%s',
                               'TIMEINDEX': '99',
                               'TYPE': 'Server Cooling Device Failure'},
 'alertCoolingDeviceNonRecoverable': {'ARGUMENTS': '{2}',
                                      'SEVERITY': 'CRITICAL',
                                      'STATE': 'DEGRADED',
                                      'SUMMARY': '%s',
                                      'TIMEINDEX': '99',
                                      'TYPE': 'Server Cooling Device Nonrecoverable'},
 'alertCoolingDeviceNormal': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'INFORMATIONAL',
                              'STATE': 'OPERATIONAL',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Cooling Device Normal'},
 'alertCoolingDeviceWarning': {'ARGUMENTS': '{2}',
                               'SEVERITY': 'MINOR',
                               'STATE': 'DEGRADED',
                               'SUMMARY': '%s',
                               'TIMEINDEX': '99',
                               'TYPE': 'Server Cooling Device Warning'},
 'alertDeviceAdd': {'ARGUMENTS': '{2}',
                    'SEVERITY': 'INFORMATIONAL',
                    'STATE': 'OPERATIONAL',
                    'SUMMARY': '%s',
                    'TIMEINDEX': '99',
                    'TYPE': 'Server Device Add'},
 'alertDeviceConfigError': {'ARGUMENTS': '{2}',
                            'SEVERITY': 'CRITICAL',
                            'STATE': 'DEGRADED',
                            'SUMMARY': '%s',
                            'TIMEINDEX': '99',
                            'TYPE': 'Server Device Config Error'},
 'alertDeviceRemove': {'ARGUMENTS': '{2}',
                       'SEVERITY': 'INFORMATIONAL',
                       'STATE': 'OPERATIONAL',
                       'SUMMARY': '%s',
                       'TIMEINDEX': '99',
                       'TYPE': 'Server Device Remove'},
 'alertFanEnclosureExtendedRemoval': {'ARGUMENTS': '{2}',
                                      'SEVERITY': 'CRITICAL',
                                      'STATE': 'DEGRADED',
                                      'SUMMARY': '%s',
                                      'TIMEINDEX': '99',
                                      'TYPE': 'Server Fan Enclosure Extended Removal'},
 'alertFanEnclosureInsertion': {'ARGUMENTS': '{2}',
                                'SEVERITY': 'INFORMATIONAL',
                                'STATE': 'OPERATIONAL',
                                'SUMMARY': '%s',
                                'TIMEINDEX': '99',
                                'TYPE': 'Server Fan Enclosure Insertion'},
 'alertFanEnclosureRemoval': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'MINOR',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Fan Enclosure Removal'},
 'alertLogFull': {'ARGUMENTS': '{2}',
                  'SEVERITY': 'CRITICAL',
                  'STATE': 'DEGRADED',
                  'SUMMARY': '%s',
                  'TIMEINDEX': '99',
                  'TYPE': 'Server Hardware Log Full'},
 'alertLogNormal': {'ARGUMENTS': '{2}',
                    'SEVERITY': 'INFORMATIONAL',
                    'STATE': 'OPERATIONAL',
                    'SUMMARY': '%s',
                    'TIMEINDEX': '99',
                    'TYPE': 'Server Hardware Log Normal'},
 'alertLogWarning': {'ARGUMENTS': '{2}',
                     'SEVERITY': 'MINOR',
                     'STATE': 'OPERATIONAL',
                     'SUMMARY': '%s',
                     'TIMEINDEX': '99',
                     'TYPE': 'Server Hardware Log Warning'},
 'alertMemoryDeviceFailure': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'CRITICAL',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Memory Device Critical'},
 'alertMemoryDeviceNonRecoverable': {'ARGUMENTS': '{2}',
                                     'SEVERITY': 'CRITICAL',
                                     'STATE': 'DEGRADED',
                                     'SUMMARY': '%s',
                                     'TIMEINDEX': '99',
                                     'TYPE': 'Server Memory Device Nonrecoverable'},
 'alertMemoryDeviceWarning': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'MINOR',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Memory Device Noncritical'},
 'alertPowerSupplyFailure': {'ARGUMENTS': '{2}',
                             'SEVERITY': 'CRITICAL',
                             'STATE': 'DEGRADED',
                             'SUMMARY': '%s',
                             'TIMEINDEX': '99',
                             'TYPE': 'Server Power Supply Failure'},
 'alertPowerSupplyNormal': {'ARGUMENTS': '{2}',
                            'SEVERITY': 'INFORMATIONAL',
                            'STATE': 'OPERATIONAL',
                            'SUMMARY': '%s',
                            'TIMEINDEX': '99',
                            'TYPE': 'Server Power Supply Normal'},
 'alertPowerSupplyWarning': {'ARGUMENTS': '{2}',
                             'SEVERITY': 'MINOR',
                             'STATE': 'DEGRADED',
                             'SUMMARY': '%s',
                             'TIMEINDEX': '99',
                             'TYPE': 'Server Power Supply Warning'},
 'alertProcessorDeviceStatusFailure': {'ARGUMENTS': '{2}',
                                       'SEVERITY': 'CRITICAL',
                                       'STATE': 'DEGRADED',
                                       'SUMMARY': '%s',
                                       'TIMEINDEX': '99',
                                       'TYPE': 'Server Processor Device Status Failure'},
 'alertProcessorDeviceStatusNormal': {'ARGUMENTS': '{2}',
                                      'SEVERITY': 'INFORMATIONAL',
                                      'STATE': 'OPERATIONAL',
                                      'SUMMARY': '%s',
                                      'TIMEINDEX': '99',
                                      'TYPE': 'Server Processor Device Status Normal'},
 'alertProcessorDeviceStatusWarning': {'ARGUMENTS': '{2}',
                                       'SEVERITY': 'MINOR',
                                       'STATE': 'DEGRADED',
                                       'SUMMARY': '%s',
                                       'TIMEINDEX': '99',
                                       'TYPE': 'Server Processor Device Status Warning'},
 'alertRedundancyDegraded': {'ARGUMENTS': '{2}',
                             'SEVERITY': 'MINOR',
                             'STATE': 'DEGRADED',
                             'SUMMARY': '%s',
                             'TIMEINDEX': '99',
                             'TYPE': 'Server Redundancy Degraded'},
 'alertRedundancyLost': {'ARGUMENTS': '{2}',
                         'SEVERITY': 'MAJOR',
                         'STATE': 'DEGRADED',
                         'SUMMARY': '%s',
                         'TIMEINDEX': '99',
                         'TYPE': 'Server Redundancy Lost'},
 'alertRedundancyNormal': {'ARGUMENTS': '{2}',
                           'SEVERITY': 'INFORMATIONAL',
                           'STATE': 'OPERATIONAL',
                           'SUMMARY': '%s',
                           'TIMEINDEX': '99',
                           'TYPE': 'Server Redundancy Normal'},
 'alertSDCardDeviceFailure': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'CRITICAL',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server SD Card Device Failure'},
 'alertSystemPeakPowerNewPeak': {'ARGUMENTS': '{2}',
                                 'SEVERITY': 'INFORMATIONAL',
                                 'STATE': 'OPERATIONAL',
                                 'SUMMARY': '%s',
                                 'TIMEINDEX': '99',
                                 'TYPE': 'Server System Peak Power New Peak'},
 'alertSystemSoftwareEvent': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'MINOR',
                              'STATE': 'OPERATIONAL',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server System Software Event'},
 'alertSystemUp': {'ARGUMENTS': '{2}',
                   'SEVERITY': 'INFORMATIONAL',
                   'STATE': 'OPERATIONAL',
                   'SUMMARY': '%s',
                   'TIMEINDEX': '99',
                   'TYPE': 'Server Administrator Startup Complete'},
 'alertTemperatureProbeFailure': {'ARGUMENTS': '{2}',
                                  'SEVERITY': 'CRITICAL',
                                  'STATE': 'DEGRADED',
                                  'SUMMARY': '%s',
                                  'TIMEINDEX': '99',
                                  'TYPE': 'Server Temperature Failure'},
 'alertTemperatureProbeNonRecoverable': {'ARGUMENTS': '{2}',
                                         'SEVERITY': 'CRITICAL',
                                         'STATE': 'DEGRADED',
                                         'SUMMARY': '%s',
                                         'TIMEINDEX': '99',
                                         'TYPE': 'Server Temperature Nonrecoverable'},
 'alertTemperatureProbeNormal': {'ARGUMENTS': '{2}',
                                 'SEVERITY': 'INFORMATIONAL',
                                 'STATE': 'OPERATIONAL',
                                 'SUMMARY': '%s',
                                 'TIMEINDEX': '99',
                                 'TYPE': 'Server Temperature Normal'},
 'alertTemperatureProbeWarning': {'ARGUMENTS': '{2}',
                                  'SEVERITY': 'MINOR',
                                  'STATE': 'DEGRADED',
                                  'SUMMARY': '%s',
                                  'TIMEINDEX': '99',
                                  'TYPE': 'Server Temperature Warning'},
 'alertThermalShutdown': {'ARGUMENTS': '{2}',
                          'SEVERITY': 'CRITICAL',
                          'STATE': 'NONOPERATIONAL',
                          'SUMMARY': '%s',
                          'TIMEINDEX': '99',
                          'TYPE': 'Server Thermal Shutdown'},
 'alertUserHostSystemReset': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'INFORMATIONAL',
                              'STATE': 'OPERATIONAL',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server User Host System Reset'},
 'alertVoltageProbeFailure': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'CRITICAL',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Voltage Failure'},
 'alertVoltageProbeNonRecoverable': {'ARGUMENTS': '{2}',
                                     'SEVERITY': 'CRITICAL',
                                     'STATE': 'DEGRADED',
                                     'SUMMARY': '%s',
                                     'TIMEINDEX': '99',
                                     'TYPE': 'Server Voltage Nonrecoverable'},
 'alertVoltageProbeNormal': {'ARGUMENTS': '{2}',
                             'SEVERITY': 'INFORMATIONAL',
                             'STATE': 'OPERATIONAL',
                             'SUMMARY': '%s',
                             'TIMEINDEX': '99',
                             'TYPE': 'Server Voltage Normal'},
 'alertVoltageProbeWarning': {'ARGUMENTS': '{2}',
                              'SEVERITY': 'MINOR',
                              'STATE': 'DEGRADED',
                              'SUMMARY': '%s',
                              'TIMEINDEX': '99',
                              'TYPE': 'Server Voltage Warning'}}