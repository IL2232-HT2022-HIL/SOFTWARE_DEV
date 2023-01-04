
import HiL_client
import HiL_client_communication
from HiL_config import *
import time

#The methods are called from the robot framework file, and the instruction functions will handle the method call
class RobotFrameworkLib():

	def open_server(self):
		HiL_client.HiL_client_setup_server_instruction(enable=True)

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
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
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
			if (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")

	def wait (self,instruction):

		string_list = instruction.split(" ")

		if (len(string_list) != 2):
			raise Exception("Client: Input not correct length, expected 2")

		elif string_list[1] not in TIME_UNITS:
			raise Exception("Client: Time unit is not supported")

		else: 
			HiL_client.HiL_client_wait_instruction(string_list)



	def push (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 5
		if (len(string_list) != 5):
			raise Exception("Client: Input not correct length, expect 4")

		#check if object is supported
		elif string_list[0] not in BINARY_OBJECTS:
			raise Exception("Client: Object is not supported")

		elif string_list[1] not in ["low", "high"]:
			raise Exception("Client: Logic type is not supported")

		elif string_list[2] != "for":
			raise Exception("Client: Missing word: for")

		elif string_list[4] not in TIME_UNITS:
			raise Exception("Client: Time unit is not supported")


		else:
			if string_list[1] == "high":
				transaction_status = HiL_client.HiL_client_push_instruction(string_list)
			else:
				transaction_status = HiL_client.HiL_client_push_low_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")

	
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
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")
	

	def set_temperature (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 4):
			raise Exception("Client: Input not correct length, expected 3")
		
		#check if object is supported
		elif string_list[1] not in SHT20_OBJECTS:
			raise Exception("Client: Object is not supported")


		elif string_list[2] != "to":
			raise Exception("Client: Missing word: to")

		else:
			transaction_status = HiL_client.HiL_client_set_temperature_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")


	def set_humidity (self,instruction):

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) != 4):
			raise Exception("Client: Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[1] not in SHT20_OBJECTS:
			raise Exception("Client: Object is not supported")
		
		elif string_list[2] != "to":
			raise Exception("Client: Missing word: to")
		
		else:
			transaction_status = HiL_client.HiL_client_set_humidity_instruction(string_list)

			#Server Error Checking
			if (transaction_status == 1):
				raise Exception("Server: Non-specified error")

			elif (transaction_status == 2):
				raise Exception("Server: Object not supported")

			elif (transaction_status == 3):
				raise Exception("Server: Non-valid requested state")
			
			elif (transaction_status != 0):
				raise Exception("Server: Should not get here, investigate")


	def check_if (self, instruction): 

		string_list = instruction.split(" ")

		#Check the length of the string, should be 3
		if (len(string_list) == 0):
			raise Exception("Client: Input not correct length, expect 3")
		
		#check if object is supported
		elif string_list[0] not in CONTROLLER_OBJECTS:
			raise Exception("CLient: Object is not supported")

		#check if object group is supported
		elif CONTROLLER_OBJECTS[string_list[0]].object_get_group not in CONTROLLER_GET_GROUPS:
			raise Exception("Client: Group is not supported")

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


	def check_logic_expression(self):
		pass



	def read_UART (self): 
	
		transaction_status,received_uart_string = HiL_client.HiL_client_read_uart_instruction()

		if (transaction_status == 1):
			raise Exception("Server: Non-specified error")

		elif (transaction_status == 2):
			raise Exception("Server: Object not supported")

		elif (transaction_status == 3):
			raise Exception("Server: Non-valid requested state")
		
		elif (transaction_status != 0):
			raise Exception("Server: Should not get here, investigate")

		else:
			print(received_uart_string)


	def view_display (self):

		transaction_status = HiL_client.HiL_client_view_display_instruction()

		if (transaction_status == 1):
			raise Exception("Server: Non-specified error")

		elif (transaction_status == 2):
			raise Exception("Server: Object not supported")

		elif (transaction_status == 3):
			raise Exception("Server: Non-valid requested state")
		
		elif (transaction_status != 0):
			raise Exception("Server: Should not get here, investigate")

		else:
			pass



# The following codes are just for debugging this file
obj = RobotFrameworkLib()
if __name__=="__main__":

	obj.open_server()

#Simple test of pushing button and reading traffic lights.

		#Default status mode on startup

	obj.wait("200 milliseconds")

	obj.check_if("TRAFFIC_LIGHTS are ALL_ON")

	obj.push("button3_center low for 100 milliseconds")

	obj.wait("2 seconds")


		#Potentiometer mode
	obj.check_if("TRAFFIC_LIGHTS are ALL_ON")

	obj.push("button3_center low for 100 milliseconds")

	obj.wait("2 seconds")


		#Humidity and temperature mode

	obj.check_if("TRAFFIC_LIGHTS are ALL_ON")

	obj.push("button3_center low for 100 milliseconds")

	obj.wait("7 seconds")


		#ENTERS LIGHT MODE but skips the first vertical_green

	obj.check_if("TRAFFIC_LIGHTS are VERTICAL_YELLOW")  # Tl2 & TL4

	obj.wait("3 seconds")

	obj.check_if("TRAFFIC_LIGHTS are ALL_RED")

	obj.wait("3 seconds")

	obj.check_if("TRAFFIC_LIGHTS are HORIZONTAL_YELLOW")  # Tl1 & TL3

	obj.wait("3 seconds")

	obj.check_if("TRAFFIC_LIGHTS are HORIZONTAL_GREEN")  # Tl1 & TL3

	obj.wait("10 seconds")

	obj.check_if("TRAFFIC_LIGHTS are HORIZONTAL_YELLOW")  # Tl1 & TL3

	obj.wait("3 seconds")

	obj.check_if("TRAFFIC_LIGHTS are ALL_RED")

	obj.push("button3_center for 100 milliseconds low")


		#Accelerometer mode
	obj.wait("200 milliseconds")
	obj.check_if("TRAFFIC_LIGHTS are ALL_ON")

	obj.push("button3_center low for 100 milliseconds")

	obj.wait("100 milliseconds")

	obj.close_server()
	
	

