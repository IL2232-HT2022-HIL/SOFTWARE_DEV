

#DEBUG LEVELS:
DEBUG_L = 1

#MACROS
DAC_RESOLUTION = 12
ADC_RESOLUTION = 12
DAC_REFERENCE = 3.3
ADC_REFERENCE = 3.3

TIME_UNITS = {
"second"         : 1,
"seconds"        : 1,
"millisecond"    : 1000, 
"milliseconds"   : 1000
}

BINARY_VALUES = {
""              : 0,
"OFF"           : 0,
"ON"            : 1
}

CONTROLLER_REQUEST = {
"CONTROLLER_REQUEST_GET"        :0,
"CONTROLLER_REQUEST_ACTUATE"    :1,   
"CONTROLLER_REQUEST_POTEN"      :2, 
"CONTROLLER_REQUEST_SHT20"      :3
}

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

SHT20_OBJECTS = {
	"TEMP_SENSOR"    : 0,
	"HUMI_SENSOR"    : 1,
}

POT_OBJECTS = {
	"POT" : 0
}

CONTROLLER_OBJECTS = BINARY_OBJECTS | SHT20_OBJECTS | POT_OBJECTS
CONTROLLER_ACTIONS = BINARY_VALUES

