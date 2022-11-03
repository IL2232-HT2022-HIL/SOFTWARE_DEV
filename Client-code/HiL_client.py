
from HiL_config import BINARY_OBJECTS, TIME_UNITS

def status_instruction():
	pass

def turn_on_instruction(instruction):

	string_list = instruction.split(" ")

	#Check the length of the string, should be 4
	if (len(string_list) != 1):
		raise Exception("Input not correct length")
	#check if object is supported
	elif string_list[0] not in BINARY_OBJECTS:
		raise Exception("object is not supported")
		
	else:
		print("acutate_{}_ON".format(string_list[0]))
		return 0

def template_instruction():
	raise Exception("THIS FUNCTION IS NOT YET IMPLEMENTED")

