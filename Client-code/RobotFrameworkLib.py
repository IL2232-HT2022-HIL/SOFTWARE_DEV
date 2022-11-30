
import HiL_client
import HiL_client_communication
from HiL_config import *
import time

#The methods are called from the robot framework file, and the instruction functions will handle the method call
class RobotFrameworkLib():

	def open_server(self):
		HiL_client.HiL_client_setup_server_instruction(enable=True)
		time.sleep(2)


	def close_server(self):
		HiL_client.HiL_client_setup_server_instruction(enable=False)


	def turn_on (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 1
		if (len(string_list) != 1):
			raise Exception("Client: Input not correct length, expect 1")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Client: Object is not supported")

		else:
			transaction_status = HiL_client.HiL_client_turn_on_instruction(string_list[0])

			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")


	def turn_off (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 1
		if (len(string_list) != 1):
			raise Exception("Client: Input not correct length, expect 1")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Client: Object is not supported")

		else:
			transaction_status = HiL_client.HiL_client_turn_off_instruction(string_list[0])

			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")


	def push (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 4
		if (len(string_list) != 4):
			raise Exception("Client: Input not correct length, expect 4")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Client: Object is not supported")


		elif string_list[1] != "for":
			raise Exception("Client: Missing word: for")


		elif string_list[3] not in TIME_UNITS:
			raise Exception("Client: Time unit is not supported")

		else:
			transaction_status = HiL_client.HiL_client_push_instruction(string_list)
			
			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")

	
	def tune (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 3):
			raise Exception("Client: Input not correct length, expect 3")

		#check if object is supported
		elif string_list[0] not in POT_OBJECTS:
			raise Exception("Client: Object is not supported")
	

		elif string_list[1] != "to":
			raise Exception("Client: Missing word: to")

		else:
			transaction_status = HiL_client.HiL_client_tune_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")
	

	def set_temperature (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 4):
			raise Exception("Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[1] not in SHT20_OBJECTS:
			raise Exception("Object is not supported")


		elif string_list[2] != "to":
			raise Exception("Missing word: to")

		else:
			transaction_status = HiL_client.HiL_client_set_temperature_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")


	def set_humidity (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 4):
			raise Exception("Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[1] not in SHT20_OBJECTS:
			raise Exception("Object is not supported")
		
		elif string_list[2] != "to":
			raise Exception("Missing word: to")
		
		else:
			transaction_status = HiL_client.HiL_client_set_humidity_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				Exception("Server: Object not supported")

			elif (transaction_status == 3):
				Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				Exception("Server: Should not get here, investigate")


	def check_if (self, instruction): 

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 3):
			raise Exception("Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[0] not in CONTROLLER_OBJECTS:
			raise Exception("Object is not supported")

		#check if object group is supported
		elif CONTROLLER_OBJECTS[string_list[0]].object_get_group not in CONTROLLER_GET_GROUPS:
			raise Exception("Group is not supported")

		else:
			transaction_status, comparison, expected_value, actual_value = HiL_client.HiL_client_check_if_instruction(string_list)

			if (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")

			else:
				if comparison is not OK:
					raise Exception("Client: Wrong reply (expected: {}, given: {})".format(expected_value,actual_value))


# The following codes are just for debuging this file
obj = RobotFrameworkLib()
if __name__=="__main__":

	obj.open_server()
	obj.turn_on("TL4_Car")
	obj.check_if("SW5 is 0")
	obj.check_if("TL4_Car is 1")
	obj.turn_off("TL4_Car")
	obj.check_if("TL4_Car is 1")



	obj.close_server()
