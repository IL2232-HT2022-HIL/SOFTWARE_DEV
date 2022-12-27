

#DEBUG LEVELS:
DEBUG_L = 0
VIRTUAL_SERVER = 0

#READABILITY ENCHANCEMENTS (DON'T MODIFY,CONSTANT VALUES)
OK = 0

#MACROS
DAC_RESOLUTION = 12
DAC_REFERENCE  = 3.3

ADC_RESOLUTION = 12
ADC_REFERENCE  = 3.3

TIME_UNITS = {
"second"         : 1,
"seconds"        : 1,
"millisecond"    : 1000, 
"milliseconds"   : 1000
}

BINARY_VALUES = {
""    : 0,
"OFF" : 0,
"ON"  : 1
}


#-----------------------------
#FOR USB COMMUNICATION:

COM_PORT      = ""
USB_BAUD_RATE = 115200


#-----------------------------
#DATA STREAM BUFFERS:

UART_BUFFER_SIZE = 128 


#-----------------------------

class ControllerObjectClass():
	def __init__(self, object_value, object_group):
		self.object_value     = object_value
		self.object_get_group = object_group

CONTROLLER_REQUEST = {
"CONTROLLER_REQUEST_GET"           :0,
"CONTROLLER_REQUEST_ACTUATE"       :1,   
"CONTROLLER_REQUEST_POTENTIOMETER" :2, 
"CONTROLLER_REQUEST_SHT20"         :3
}
		
CONTROLLER_GET_GROUPS = {
"CONTROLLER_GET_GROUP_BINARY"         : ControllerObjectClass(0 ,"CONTROLLER_GET_GROUP_BINARY"),
"CONTROLLER_GET_GROUP_PWM"            : ControllerObjectClass(1, "CONTROLLER_GET_GROUP_PWM"),
"CONTROLLER_GET_GROUP_POT_OBJECTS"    : ControllerObjectClass(2 ,"CONTROLLER_GET_GROUP_POT_OBJECTS"),
"CONTROLLER_GET_GROUP_DATA_STREAMS"   : ControllerObjectClass(3 ,"CONTROLLER_GET_GROUP_DATA_STREAMS"),
"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS" : ControllerObjectClass(4 ,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS")
}

BINARY_OBJECTS = {
"SW5"             : ControllerObjectClass(0 ,"CONTROLLER_GET_GROUP_BINARY"),
"SW6"             : ControllerObjectClass(1 ,"CONTROLLER_GET_GROUP_BINARY"),
"SW7"             : ControllerObjectClass(2 ,"CONTROLLER_GET_GROUP_BINARY"),
"SW8"             : ControllerObjectClass(3 ,"CONTROLLER_GET_GROUP_BINARY"),
"button3_A"       : ControllerObjectClass(4 ,"CONTROLLER_GET_GROUP_BINARY"),
"button3_B"       : ControllerObjectClass(5 ,"CONTROLLER_GET_GROUP_BINARY"),
"button3_C"       : ControllerObjectClass(6 ,"CONTROLLER_GET_GROUP_BINARY"),
"button3_D"       : ControllerObjectClass(7 ,"CONTROLLER_GET_GROUP_BINARY"),
"button3_center"  : ControllerObjectClass(8 ,"CONTROLLER_GET_GROUP_BINARY"),
"TL1_Car"         : ControllerObjectClass(9 ,"CONTROLLER_GET_GROUP_BINARY"),
"TL2_Car"         : ControllerObjectClass(10,"CONTROLLER_GET_GROUP_BINARY"),
"TL3_Car"         : ControllerObjectClass(11,"CONTROLLER_GET_GROUP_BINARY"),
"TL4_Car"         : ControllerObjectClass(12,"CONTROLLER_GET_GROUP_BINARY"),

"USR_LED1"        : ControllerObjectClass(13,"CONTROLLER_GET_GROUP_BINARY"),
"USR_LED2"		  : ControllerObjectClass(14,"CONTROLLER_GET_GROUP_BINARY")
}

SHT20_OBJECTS  = {
"TEMP_SENSOR"     : ControllerObjectClass(0 ,"SHT20_OBJECTS"),
"HUMI_SENSOR"     : ControllerObjectClass(1 ,"SHT20_OBJECTS"),
}

POT_OBJECTS    = {
"Poti"            : ControllerObjectClass(0 ,"CONTROLLER_GET_GROUP_POT_OBJECTS")
}

PWM_OBJECTS = {
"PWM_MEASUREMENT" : ControllerObjectClass(0,"CONTROLLER_GET_GROUP_PWM")
}

DATA_STREAM_OBJECTS = {
"UART"            : ControllerObjectClass(0,"CONTROLLER_GET_GROUP_DATA_STREAMS"),
"DISPLAY"		  : ControllerObjectClass(1,"CONTROLLER_GET_GROUP_DATA_STREAMS"),
}


TRAFFIC_LIGHT_OBJECTS = {

#ORDER IN BINARY:
#(MSB) TL1_R, TL1_Y, TL1_G, PL1_R, PL1_G, PL1_B, TL2_R, TL2_Y, TL2_G, ->
#   -> PL2_R, PL2_G, PL2_B, TL3_R, TL3_Y, TL3_G, TL4_R, TL4_Y, TL4_G (LSB)


"TRAFFIC_LIGHTS"    : ControllerObjectClass(0x1ff,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),	

#predefines states
"ALL_ON"            : ControllerObjectClass(0x1ff,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"ALL_RED"	        : ControllerObjectClass(0b001001001001001001,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"HORIZONTAL_YELLOW" : ControllerObjectClass(0b001010001001001010,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"HORIZONTAL_GREEN"  : ControllerObjectClass(0b001100001001001100,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"VERTICAL_YELLOW"   : ControllerObjectClass(0b010001001010001001,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"VERTICAL_GREEN"    : ControllerObjectClass(0b100001001100001001,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

#individual states
"TL1_RED"           : ControllerObjectClass(1<<0,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL1_YELLOW"        : ControllerObjectClass(1<<1,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL1_GREEN"         : ControllerObjectClass(1<<2,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"PL1_RED"           : ControllerObjectClass(1<<3,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"PL1_GREEN"         : ControllerObjectClass(1<<4,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"PL1_BLUE"          : ControllerObjectClass(1<<5,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"TL2_RED"           : ControllerObjectClass(1<<6,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL2_YELLOW"        : ControllerObjectClass(1<<7,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL2_GREEN"         : ControllerObjectClass(1<<8,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),


"PL2_RED"           : ControllerObjectClass(1<<9,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"PL2_GREEN"         : ControllerObjectClass(1<<10,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"PL2_BLUE"          : ControllerObjectClass(1<<11,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"TL3_RED"           : ControllerObjectClass(1<<12,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL3_YELLOW"        : ControllerObjectClass(1<<13,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL3_GREEN"         : ControllerObjectClass(1<<14,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),

"TL4_RED"           : ControllerObjectClass(1<<15,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL4_YELLOW"        : ControllerObjectClass(1<<16,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS"),
"TL4_GREEN"         : ControllerObjectClass(1<<17,"CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS")

}


CONTROLLER_OBJECTS = CONTROLLER_GET_GROUPS | BINARY_OBJECTS | SHT20_OBJECTS | POT_OBJECTS | PWM_OBJECTS | DATA_STREAM_OBJECTS | TRAFFIC_LIGHT_OBJECTS
CONTROLLER_ACTIONS = BINARY_VALUES 
