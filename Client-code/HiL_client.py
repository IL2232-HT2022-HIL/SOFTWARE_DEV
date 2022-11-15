import time
import HiL_client_communication
from HiL_config import CONTROLLER_OBJECTS, TIME_UNITS, ADC_RESOLUTION, DAC_RESOLUTION, DAC_REFERENCE, ADC_REFERENCE, DEBUG_L


def HiL_client_POTEN_DAC(decimal_string):
    
    decimal_value = float(decimal_string)
    bit_value     = int(round(2**ADC_RESOLUTION*(decimal_value)/ADC_REFERENCE))
   
    int_upper = (bit_value >> 8) & 0xff
    int_lower =        bit_value & 0xff

    if DEBUG_L:
    	print("Your value will be rounded.")
    	print(bit_value)

    return [int_lower,int_upper]


def HiL_client_status_instruction():
	#to be filled as a setup function
	pass


def HiL_client_turn_on_instruction(binary_object):

	python_instruction = "CONTROLLER_REQUEST_ACTUATE " + binary_object + " ON"
	encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
	
	if DEBUG_L:
		print(python_instruction)
		print(encoded_message)


def HiL_client_turn_off_instruction(binary_object):

	python_instruction = "CONTROLLER_REQUEST_ACTUATE " + binary_object + " OFF"
	encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)

	if DEBUG_L:
		print(python_instruction)
		print(encoded_message)


def HiL_client_push_instruction(string_list):

	binary_object = string_list[0]
	wait_time     = int (string_list[2])
	time_unit     = string_list[3]


	HiL_client_turn_on_instruction(binary_object)

	
	print("Pushing {} for {} {}...".format(binary_object, wait_time, time_unit))
	sleep_time = wait_time / (TIME_UNITS[time_unit])
	time.sleep(sleep_time)


	HiL_client_turn_off_instruction(binary_object)


def HiL_client_tune_instruction(string_list):

	controller_object = string_list[0]
	decimal_value     = float(string_list[2])
	split_integer     = [str(i) for i in HiL_client_POTEN_DAC(decimal_value)]

	python_instruction = "CONTROLLER_REQUEST_POTEN {} {} {}".format(controller_object,split_integer[0],split_integer[1])
	encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)

	if DEBUG_L:
		print(python_instruction)
		print(encoded_message)


def HiL_client_set_temp_instruction(string_list):

	python_instruction = "CONTROLLER_REQUEST_SHT20 {} {}".format(string_list[0], string_list[2])
	encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)

	if DEBUG_L:
		print(python_instruction)
		print(encoded_message)


def HiL_client_set_humi_instruction(string_list):

	python_instruction = "CONTROLLER_REQUEST_SHT20 {} {}".format(string_list[0], string_list[2])
	encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
	
	if DEBUG_L:
		print(python_instruction)
		print(encoded_message)
	

def template_instruction():
	#is left for adding any other keywords
	raise Exception("THIS FUNCTION IS NOT YET IMPLEMENTED")

# The following codes are just for debuging this file
if __name__=="__main__":
	pass