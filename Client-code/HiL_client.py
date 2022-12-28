
import time
import HiL_client_communication
from HiL_config import *


def HiL_client_DAC_conversion(decimal_string, conversion_type = "encode"):
    
	
	decimal_value = float(decimal_string)
	bit_value     = int ( round(2**ADC_RESOLUTION*(decimal_value)/ADC_REFERENCE) )
	
	if conversion_type == "decode":
		return bit_value

	elif conversion_type == "encode":

		int_upper = (bit_value >> 8) & 0xff
		int_lower =        bit_value & 0xff

		if DEBUG_L:
			print("Your value will be rounded.")
			print(bit_value)

		return [int_lower,int_upper]


def HiL_client_SHT20_humidity_conversion(decimal_string):

	# RH = -6 + 125 * S_RH/(2**16)	

	decimal_value = float(decimal_string)

	bit_value = int ( round( (decimal_value + 6)*(2**16) / 125 ) )

	int_upper = (bit_value >> 8) & 0xff
	int_lower = bit_value & 0xff

	if DEBUG_L:
		print("Your value will be rounded.")
		print(bit_value)

	return [int_lower,int_upper]


def HiL_client_SHT20_temperature_conversion(decimal_string):

	# T = -46.85 + 175.72 * S_t/(2**16)
	
	decimal_value = float(decimal_string)
	bit_value = int ( round( (decimal_value + 46.85)*(2**16) / 175.72 ) )

	int_upper = (bit_value >> 8) & 0xff
	int_lower = bit_value & 0xff

	if DEBUG_L:
		print("Your value will be rounded.")
		print(bit_value)

	return [int_lower,int_upper]


def HiL_client_transaction(instrucion_string):

	encoded_message = HiL_client_communication.HiL_client_communication_encode(instrucion_string)
	HiL_client_communication.HiL_client_communication_transmit(encoded_message)

	recieved_message_array = HiL_client_communication.HiL_client_communication_receive()
	transaction_status = HiL_client_communication.HiL_client_communication_decode(recieved_message_array)

	if DEBUG_L:
		print(instrucion_string)
		print(encoded_message)

	return transaction_status

def HiL_client_setup_server_instruction(enable):
	HiL_client_communication.HiL_client_communication_serial_port(enable)


def HiL_client_turn_on_instruction(binary_object):

	python_instruction = "CONTROLLER_REQUEST_ACTUATE " + binary_object + " ON"
	return HiL_client_transaction(python_instruction)


def HiL_client_turn_off_instruction(binary_object):

	python_instruction = "CONTROLLER_REQUEST_ACTUATE " + binary_object + " OFF"
	return HiL_client_transaction(python_instruction)


def HiL_client_wait_instruction(string_list):

	wait_time  = float(string_list[0])
	time_unit  = string_list[1]

	sleep_time = wait_time / (TIME_UNITS[time_unit])
	time.sleep(sleep_time)
	

def HiL_client_push_instruction(string_list):

	binary_object = string_list[0]
	wait_time     = float(string_list[2])
	time_unit     = string_list[3]

	transaction_status = HiL_client_turn_on_instruction(binary_object)

	if transaction_status is not OK:
		return transaction_status # something bad happened, return error code


	print("Pushing {} for {} {}...".format(binary_object, wait_time, time_unit))
	sleep_time = wait_time / (TIME_UNITS[time_unit])
	time.sleep(sleep_time)


	transaction_status = HiL_client_turn_off_instruction(binary_object)
	return transaction_status


def HiL_client_tune_instruction(string_list):

	controller_object = string_list[0]
	decimal_value     = float(string_list[2])
	split_integer     = [str(i) for i in HiL_client_DAC_conversion(decimal_value)]

	python_instruction = "CONTROLLER_REQUEST_POTENTIOMETER {} {} {}".format(controller_object,split_integer[0],split_integer[1])
	return HiL_client_transaction(python_instruction)


def HiL_client_set_temperature_instruction(string_list):

	controller_object = string_list[1]
	decimal_value     = float(string_list[3])
	split_integer     = [str(i) for i in HiL_client_SHT20_temperature_conversion(decimal_value)]

	python_instruction = "CONTROLLER_REQUEST_SHT20 {} {} {}".format(controller_object,split_integer[0],split_integer[1])
	return HiL_client_transaction(python_instruction)


def HiL_client_set_humidity_instruction(string_list):

	controller_object = string_list[1]
	decimal_value     = float(string_list[3])
	split_integer     = [str(i) for i in HiL_client_SHT20_humidity_conversion(decimal_value)]

	python_instruction = "CONTROLLER_REQUEST_SHT20 {} {} {}".format(controller_object,split_integer[0],split_integer[1])
	return HiL_client_transaction(python_instruction)




def HiL_client_read_shift_register_instruction(controller_object):

	object_group = CONTROLLER_OBJECTS[controller_object].object_get_group

	received_shift_register_state = 0 # every bit, starting from 0 represent a led 

	for frame_index in range(2):
	
		python_instruction = "CONTROLLER_REQUEST_GET {} {}".format(object_group,frame_index) #zero indicates reset pointer
		print(python_instruction) 
		reply = HiL_client_transaction(python_instruction)

		print(bin(reply))

		transaction_status = (reply >> 12) & 0xff # status code embedded in last 4 bits
		received_frame = (reply & 0x1ff) # extract 9 led state from frame

		if (transaction_status != 0):
			return transaction_status, -1

		received_shift_register_state += (received_frame << frame_index*9)


	if (CONTROLLER_OBJECTS[controller_object].object_value != 100):
		index_to_extract = CONTROLLER_OBJECTS[controller_object].object_value

		if (received_shift_register_state & index_to_extract) == index_to_extract:
			controller_object_state = bin(1) 
		else:
			controller_object_state = bin(0)

	else:
		controller_object_state = bin(received_shift_register_state)

	return transaction_status, controller_object_state


def HiL_client_check_if_instruction(string_list):

	controller_object = string_list[0]
	object_group = CONTROLLER_OBJECTS[controller_object].object_get_group
	expected_value_string = " ".join(string_list[2:])
	
	if object_group == "CONTROLLER_GET_GROUP_DATA_STREAMS":

		if controller_object == "UART":
			transaction_status, received_value = HiL_client_read_uart_instruction()
			expected_value = expected_value_string
	
		else:
			transaction_status = 2
			received_value = 0
			expected_value = 0


	elif object_group == "CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS":
		
		#extract shift register content
		transaction_status, received_value = HiL_client_read_shift_register_instruction(controller_object)
	
		if CONTROLLER_OBJECTS[controller_object].object_value != 100:
			expected_value = bin(int(expected_value_string))
		
		else:
			expected_value = bin(CONTROLLER_OBJECTS[expected_value_string].object_value)

	else:

		python_instruction = "CONTROLLER_REQUEST_GET {} {}".format(object_group,controller_object)
		reply = HiL_client_transaction(python_instruction)

		# reply includes two bits of information: the status code of the request 
		# and the actual value that is requested. bit 0-11 = value, bit 12-15 = status code

		transaction_status = (reply >> 12) & 0xff # error code embedded in last 4 bits
		received_value     = (reply & 0xfff)      # actual useful value 

		if object_group == "CONTROLLER_GET_GROUP_BINARY":
			expected_value = int(expected_value_string)
			
		elif object_group == "CONTROLLER_GET_GROUP_PWM":
			expected_value = int(expected_value_string)

		elif object_group == "POT_OBJECTS":
			expected_value = HiL_client_DAC_conversion(float(expected_value_string),"decode")

	
	comparison = OK if received_value == expected_value else not OK 

	return transaction_status, comparison, expected_value, received_value 


def HiL_client_read_uart_instruction():
	
	controller_object = "UART"
	object_group = CONTROLLER_OBJECTS[controller_object].object_get_group

	uart_buffer = [] # used as input buffer from UART

	# resets buffer pointer in server 
	python_instruction = "CONTROLLER_REQUEST_GET {} {} {}".format(object_group,controller_object,0) #zero indicates reset pointer 
	reply = HiL_client_transaction(python_instruction)

	transaction_status = (reply >> 12) & 0xff # status code embedded in last 4 bits
	received_character = chr((reply & 0xfff)) # actual useful value 

	if (transaction_status != 0):
		return transaction_status 

	counter = 0
	while True: #do-while 
		python_instruction = "CONTROLLER_REQUEST_GET {} {} {}".format(object_group,controller_object,1) #one indicates get value and increment pointer 
		reply = HiL_client_transaction(python_instruction)

		transaction_status = (reply >> 12) & 0xff # status code embedded in last 4 bits
		received_character = chr((reply & 0xfff)) # actual useful value 
		
		if (counter == UART_BUFFER_SIZE) or (transaction_status != 0) or received_character == '\00':
			break
		else:
			uart_buffer.append(received_character) # received character added to buffer
			counter += 1

	received_uart_string = ''.join(uart_buffer)

	return transaction_status, received_uart_string


def HiL_client_view_display_instruction():
	
	controller_object = "DISPLAY"
	object_group = CONTROLLER_OBJECTS[controller_object].object_get_group

	display_buffer = []

	#reset_pointer 
	python_instruction = "CONTROLLER_REQUEST_GET {} {} {}".format(object_group,controller_object,0) #resets buffer pointer
	reply = HiL_client_transaction(python_instruction)

	transaction_status = (reply >> 12) & 0xff # status code embedded in last 4 bits
	received_character = chr((reply & 0xfff)) # actual useful value 

	if (transaction_status != 0):
		return transaction_status 

	for i in range(10):
		python_instruction = "CONTROLLER_REQUEST_GET {} {} {}".format(object_group,controller_object,1) #gets buffer content and increment pointer
		reply = HiL_client_transaction(python_instruction)

	return 0
