
CHANGE_REQUEST = {
"ACTUATE"        :80,
"POTEN"          :1,
"SHT20"          :2,
}

CONTROLLER_REQUEST = {
"CONTROLLER_REQUEST_GET"        :0,
"CONTROLLER_REQUEST_ACTUATE"    :1,   
}



DAC_RESOLUTION = 12
ADC_RESOLUTION = 12
DAC_REFERENCE = 3.3
ADC_REFERENCE = 3.3

BINARY_OBJECTS = {
"SW5"            : 0,
"SW6"            : 1,
"SW7"            : 2,
"SW8"            : 3,
"button3_A"      : 4,
"button3_B"      : 5,
"button3_C"      : 6,
"button3_D"      : 7,
"button3_center" : 8,
"TL1_Car"        : 9,
"TL2_Car"        : 10,
"TL3_Car"        : 11,
"TL4_Car"        : 12,
}

BINARY_VALUE = {
"OFF"           : 0,
"ON"            : 1,
}

SHT20_OBJECTS = {
"TEMP_SENSOR"    : 0,
"HUMI_SENSOR"    : 1,
}

'''
VALUE_BASED_OBJECTS = {
"POT"            : 0,
"TEMP_SENSOR"    : 1,
"HUMI_SENSOR"    : 2,
}
'''


TIME_UNITS = {
"second"         : 1,
"seconds"        : 1,
"millisecond"    : 1000, 
"milliseconds"   : 1000
}