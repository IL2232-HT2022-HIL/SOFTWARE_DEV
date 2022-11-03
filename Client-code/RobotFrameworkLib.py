

from HiL_client import status_instruction, turn_on_instruction, template_instruction

#This class will be dealing with the robot framework interface 
class RobotFrameworkLib():

	def run_status(self):
		status_instruction()

	def turn_on (self,instruction):
		turn_on_instruction(instruction)

	def template_keyword(self):
		template_instruction()


obj = RobotFrameworkLib()

