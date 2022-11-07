import time
from HiL_config import BINARY_OBJECTS, TIME_UNITS

def status_instruction():
	#to be filled as a setup function
	pass

def turn_on_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 1
	if (len(string_list) != 1):
		raise Exception("Input not correct length, expect 1")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("Object is not supported")
		
	else:
		print("acutate_{}_ON".format(string_list[0]))
		return 0

def turn_off_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 1
	if (len(string_list) != 1):
		raise Exception("Input not correct length, expect 1")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("Object is not supported")
		
	else:
		print("acutate_{}_OFF".format(string_list[0]))
		return 0

def push_instruction(instruction):

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
		print("acutate_{}_ON".format(string_list[0]))
		sleep_time = int(string_list[2]) / (TIME_UNITS[string_list[3]])
		#print(sleep_time)
		print("Pushing {} for {} {}...".format(string_list[0], string_list[2], string_list[3]))
		time.sleep(sleep_time)
		print("acutate_{}_OFF".format(string_list[0]))
		return 0

def tune_instruction(instruction):

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
		print("The value of {} is set to {}V.".format(string_list[0], string_list[2]))
		return 0

def set_temp_instruction(instruction):

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
		print("The temperature on {} is set to {} Celsius degree.".format(string_list[0], string_list[2]))
		return 0

def set_humi_instruction(instruction):

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
		print("The humidity on {} is set to {}%.".format(string_list[0], string_list[2]))
		return 0

def template_instruction():
	#is left for adding any other keywords
	raise Exception("THIS FUNCTION IS NOT YET IMPLEMENTED")

# The following codes are just for debuging this file
if __name__=="__main__":
    #push_instruction("button3_A for 3 seconds")
	set_temp_instruction("TEMP_SENSOR to 35")
	set_humi_instruction("HUMI_SENSOR to 44.5")