

#from HiL_client import status_instruction, turn_on_instruction, template_instruction
import HiL_client
import HiL_client_communication
from HiL_config import BINARY_OBJECTS, TIME_UNITS

#The mathods are called from the robot framework file, and the instruction functions will handle the method call
class RobotFrameworkLib():

	def run_status(self):
		HiL_client.HiL_client_status_instruction() #diagnostics


	def turn_on (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 1
		if (len(string_list) != 1):
			raise Exception("Input not correct length, expect 1")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Object is not supported")

		else:
			HiL_client.HiL_client_turn_on_instruction(string_list[0])


	def turn_off (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 1
		if (len(string_list) != 1):
			raise Exception("Input not correct length, expect 1")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Object is not supported")

		else:
			HiL_client.HiL_client_turn_off_instruction(string_list[0])
	

	def push (self,instruction):

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
			HiL_client.HiL_client_push_instruction(string_list)
	
	def tune (self,instruction):

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
			HiL_client.HiL_client_tune_instruction(string_list)
	


	def set_temp (self,instruction):

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
			HiL_client.HiL_client_set_temp_instruction(string_list)

	def set_humi (self,instruction):

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
			HiL_client.HiL_client_set_humi_instruction(string_list)

	def template_keyword(self):
		HiL_client.template_instruction()

# The following codes are just for debuging this file
obj = RobotFrameworkLib()
if __name__=="__main__":
	obj.tune("POT to 1.2")
