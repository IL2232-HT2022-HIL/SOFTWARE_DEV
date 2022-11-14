import time
import HiL_client_communication
from HiL_config import BINARY_OBJECTS, TIME_UNITS

def status_instruction():
	#to be filled as a setup function
	pass

def HiL_client_turn_on_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 1
	if (len(string_list) != 1):
		raise Exception("Input not correct length, expect 1")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("Object is not supported")
		
	else:
		python_instruction = "ACTUATE "+string_list[0]+" ON"
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		#return 0

def HiL_client_turn_off_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 1
	if (len(string_list) != 1):
		raise Exception("Input not correct length, expect 1")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("Object is not supported")
		
	else:
		#print("ACTUATE_{}_OFF".format(string_list[0]))
		python_instruction = "ACTUATE "+string_list[0]+" OFF"
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		return 0

def HiL_client_push_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 4
	if (len(string_list) != 4):
		raise Exception("Input not correct length, expect 4")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("Object is not supported")
	elif string_list[1] != "for":
		raise Exception("Missing word: for")
	elif string_list[3] not in TIME_UNITS:
		raise Exception("Time unit is not supported")
	else:
		#print("ACTUATE_{}_ON".format(string_list[0]))
		python_instruction = "ACTUATE "+string_list[0]+" ON"
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		
		sleep_time = int(string_list[2]) / (TIME_UNITS[string_list[3]])
		#print(sleep_time)
		print("Pushing {} for {} {}...".format(string_list[0], string_list[2], string_list[3]))
		time.sleep(sleep_time)

		#print("ACTUATE_{}_OFF".format(string_list[0]))
		python_instruction = "ACTUATE "+string_list[0]+" OFF"
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		#return 0

def HiL_client_tune_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 3
	if (len(string_list) != 3):
		raise Exception("Input not correct length, expect 3")
	#check if object is supported
	elif string_list[0] != "POT":
		raise Exception("Object is not supported, should be POT")
	elif string_list[1] != "to":
		raise Exception("Missing word: to")
	else:
		#print("POTEN_{}_{}".format(string_list[0], string_list[2]))
		#print("The value of {} is set to {}V.".format(string_list[0], string_list[2]))
		python_instruction = "POTEN "+string_list[0]+" "+string_list[2]
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		#return 0

def HiL_client_set_temp_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 3
	if (len(string_list) != 3):
		raise Exception("Input not correct length, expect 3")
	#check if object is supported
	elif string_list[0] != "TEMP_SENSOR":
		raise Exception("Object is not supported, should be TEMP_SENSOR")
	elif string_list[1] != "to":
		raise Exception("Missing word: to")
	else:
		#print("SHT20_{}_{}".format(string_list[0], string_list[2]))
		#print("The temperature on {} is set to {} Celsius degree.".format(string_list[0], string_list[2]))
		python_instruction = "SHT20 "+string_list[0]+" "+string_list[2]
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		#return 0

def HiL_client_set_humi_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 3
	if (len(string_list) != 3):
		raise Exception("Input not correct length, expect 3")
	#check if object is supported
	elif string_list[0] != "HUMI_SENSOR":
		raise Exception("Object is not supported, should be HUMI_SENSOR")
	elif string_list[1] != "to":
		raise Exception("Missing word: to")
	else:
		#print("SHT20_{}_{}".format(string_list[0], string_list[2]))
		#print("The humidity on {} is set to {}%.".format(string_list[0], string_list[2]))
		python_instruction = "SHT20 "+string_list[0]+" "+string_list[2]
		print(python_instruction)
		encoded_message = HiL_client_communication.HiL_client_communication_encode(python_instruction)
		print(encoded_message)
		#return 0

def template_instruction():
	#is left for adding any other keywords
	raise Exception("THIS FUNCTION IS NOT YET IMPLEMENTED")

# The following codes are just for debuging this file
if __name__=="__main__":
	HiL_client_turn_on_instruction("button3_A")
	HiL_client_tune_instruction("POT to 2.8")
	HiL_client_set_temp_instruction("TEMP_SENSOR to 35")
	HiL_client_set_humi_instruction("HUMI_SENSOR to 44.5")