

#from HiL_client import status_instruction, turn_on_instruction, template_instruction
import HiL_client

#This class will be dealing with the robot framework interface 
class RobotFrameworkLib():

	def run_status(self):
		HiL_client.status_instruction()

	def turn_on (self,instruction):
		HiL_client.turn_on_instruction(instruction)

	def turn_off (self,instruction):
		HiL_client.turn_off_instruction(instruction)
	
	def push (self,instruction):
		HiL_client.push_instruction(instruction)
	
	def tune (self,instruction):
		HiL_client.tune_instruction(instruction)
	
	def set_temp (self,instruction):
		HiL_client.set_temp_instruction(instruction)

	def set_humi (self,instruction):
		HiL_client.set_humi_instruction(instruction)

	def template_keyword(self):
		HiL_client.template_instruction()



# The following codes are just for debuging this file
obj = RobotFrameworkLib()
if __name__=="__main__":
	obj.tune("POT to 1.8")
