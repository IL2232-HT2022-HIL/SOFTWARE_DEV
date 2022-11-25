
import HiL_client
from HiL_config import CONTROLLER_OBJECTS, CONTROLLER_GET_GROUPS, BINARY_OBJECTS, POT_OBJECTS, SHT20_OBJECTS, TIME_UNITS

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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid state request")
			
			else:
				raise Exception("Server: Should not get here, investigate")


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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid state request")
			
			else:
				raise Exception("Server: Should not get here, investigate")


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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				print("Server: Non-specified error")

			elif (transaction_status == 2):
				print("Server: Object not supported")

			elif (transaction_status == 3):
				print("Server: Non-valid requested state")
			
			else:
				print("Server: Should not get here, investigate")

	
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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				print("Server: Non-specified error")

			elif (transaction_status == 2):
				print("Server: Object not supported")

			elif (transaction_status == 3):
				print("Server: Non-valid requested state")
			
			else:
				print("Server: should not get here, investigate")
	

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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				print("Server: Non-specified error")

			elif (transaction_status == 2):
				print("Server: Object not supported")

			elif (transaction_status == 3):
				print("Server: Non-valid requested state")
			
			else:
				print("Server: Should not get here, investigate")


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
			if (transaction_status == 0):
				pass
			
			elif (transaction_status == 1):
				print("Server: Non-specified error")

			elif (transaction_status == 2):
				print("Server: Object not supported")

			elif (transaction_status == 3):
				print("Server: Non-valid requested state")
			
			else:
				print("Server: Should not get here, investigate")


	def check_if (self, instruction): 

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 3):
			raise Exception("Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[0] not in CONTROLLER_OBJECTS:
			raise Exception("Object is not supported")

		elif CONTROLLER_OBJECTS[string_list[0]].object_get_group not in CONTROLLER_GET_GROUPS:
			raise Exception("Group is not supported")

		else:
			reply = HiL_client.HiL_client_check_if_instruction(string_list)

			if int(string_list[2]) != reply:
				raise Exception("Wrong reply (expected: {}, given: {})".format(string_list[2],reply))


# The following codes are just for debuging this file
obj = RobotFrameworkLib()
if __name__=="__main__":

	obj.open_server()
	obj.turn_on("SW5")
	obj.close_server()
