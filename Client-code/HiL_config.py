

#DEBUG LEVELS:
DEBUG_L = 0
VIRTUAL_SERVER = 0

#READABILITY
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
"CONTROLLER_GET_GROUP_BINARY"       : ControllerObjectClass(0 ,"CONTROLLER_GET_GROUP_BINARY"),
"CONTROLLER_GET_GROUP_PWM"          : ControllerObjectClass(1, "CONTROLLER_GET_GROUP_PWM"),
"CONTROLLER_GET_GROUP_POT_OBJECTS"  : ControllerObjectClass(2 ,"CONTROLLER_GET_GROUP_POT_OBJECTS"),
"CONTROLLER_GET_GROUP_DATA_STREAMS" : ControllerObjectClass(3 ,"CONTROLLER_GET_GROUP_DATA_STREAMS"),
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
"DISPLAY"		  : ControllerObjectClass(1,"CONTROLLER_GET_GROUP_DATA_STREAMS")
}


CONTROLLER_OBJECTS = CONTROLLER_GET_GROUPS | BINARY_OBJECTS | SHT20_OBJECTS | POT_OBJECTS | PWM_OBJECTS | DATA_STREAM_OBJECTS
CONTROLLER_ACTIONS = BINARY_VALUES 
