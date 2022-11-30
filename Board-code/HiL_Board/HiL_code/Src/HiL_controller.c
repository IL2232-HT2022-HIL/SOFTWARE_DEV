/*
 * _controller.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */

#include "HiL_controller.h"

int recieved_data[4];
int controller_reply[2];


void HiL_controller_copy_array(int* to_be_copied)
{
	for (int i = 0; i<4; i++)
	{
		recieved_data[i] = to_be_copied[i];
	}
}

//parses message, and tries to execute commands.
void HiL_controller_read_message(int* recieved_data)
{
	//reset status array
	controller_reply[CONTROLLER_VALUE1] = 0;
	controller_reply[CONTROLLER_VALUE2] = 0;

	// gets newest instruction
	HiL_controller_copy_array(recieved_data);

	// identify the message content
	switch(recieved_data[CONTROLLER_REQUEST])
	{

		case CONTROLLER_REQUEST_GET: 

			HiL_controller_send_message();
			break;


		case CONTROLLER_REQUEST_ACTUATE:
			
			controller_reply[CONTROLLER_VALUE1] =  HiL_mcu_commands_binary_action(
													recieved_data[CONTROLLER_OBJECT],
													recieved_data[CONTROLLER_ACTION1]);
			
			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
		                                 controller_reply[CONTROLLER_VALUE2]);			
			break;


		case CONTROLLER_REQUEST_POTENTIOMETER:
	

			controller_reply[CONTROLLER_VALUE1] = HiL_mcu_commands_potentiometer_emulator(
													recieved_data[CONTROLLER_ACTION1],
													recieved_data[CONTROLLER_ACTION2]);

			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
		                                 controller_reply[CONTROLLER_VALUE2]);

			break;
			

		case CONTROLLER_REQUEST_SHT20:
			
			controller_reply[CONTROLLER_VALUE1] = CONTROLLER_ERROR_NO_SUPPORT;

			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
		                                 controller_reply[CONTROLLER_VALUE2]);
			
			break;


		default: 

			// Reply with error
			controller_reply[CONTROLLER_VALUE1] = CONTROLLER_ERROR_UNSPECIFIED;

			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
		                                 controller_reply[CONTROLLER_VALUE2]);
			
	}	
}

void HiL_controller_send_message()
{
	
	switch(recieved_data[CONTROLLER_GET_GROUP])
	{
		
		case CONTROLLER_GET_GROUP_BINARY:
			
			controller_reply[CONTROLLER_VALUE1] = HiL_mcu_commands_binary_status(recieved_data[CONTROLLER_GET_OBJECT]);
			
			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
		                                 controller_reply[CONTROLLER_VALUE2]);
			break;


		default:
			// Reply with error
			controller_reply[CONTROLLER_VALUE1] = CONTROLLER_ERROR_NO_SUPPORT;
			HiL_gateway_transmit_message(0,32);
	}
}




