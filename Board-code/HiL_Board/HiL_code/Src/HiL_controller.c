/*
 * _controller.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */

#include "HiL_controller.h"
#include "cmsis_os.h"
#include "HiL_MSGQ.h"

extern uint8_t Duty;

extern uint8_t light_state[];

static uint8_t recieved_data[HiL_MSGQ_Buf_arr_len];
	   uint8_t controller_reply[2];
	   uint8_t controller_reply2[2];

void HiL_controller_copy_array(uint8_t* to_be_copied)
{
	for (uint8_t i = 0; i<HiL_MSGQ_Buf_arr_len; i++)
	{
		recieved_data[i] = to_be_copied[i];
	}
}

//parses message, and tries to execute commands.
void HiL_controller_read_message(uint8_t* recieved_data)
{
	//reset status array
	controller_reply[CONTROLLER_VALUE1] = 0;
	controller_reply[CONTROLLER_VALUE2] = 0;
	controller_reply2[CONTROLLER_VALUE1] = 0;
	controller_reply2[CONTROLLER_VALUE2] = 0;

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

		case CONTROLLER_GET_GROUP_PWM:


			controller_reply[CONTROLLER_VALUE1] = HiL_mcu_commands_PWM_measure();

			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
										 controller_reply[CONTROLLER_VALUE2]);

			break;

		case CONTROLLER_GET_GROUP_DATA_STREAMS:

			if (recieved_data[CONTROLLER_GET_OBJECT] == DATA_STREAM_OBJECTS_UART)
			{

				uint16_t function_return = HiL_mcu_commands_UART_handler(recieved_data[CONTROLLER_GET_ACTION]);

				controller_reply[CONTROLLER_VALUE1] =  function_return       & 0xff;
				controller_reply[CONTROLLER_VALUE2] = (function_return >> 8) & 0xff;

				HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
										     controller_reply[CONTROLLER_VALUE2]);

				break;

			}

		case CONTROLLER_GET_GROUP_TRAFFIC_LIGHTS:
				// WORK IN PROGRESS
			{

			uint32_t light_state_variable  = light_state[0];
					 light_state_variable |= light_state[1] << 6;
					 light_state_variable |= light_state[2] << 12;

			if (recieved_data[CONTROLLER_GET_OBJECT] == 1)
			{
				light_state_variable = light_state_variable >> 9;
			}
			else // do nothing
			{}

			controller_reply[CONTROLLER_VALUE1] = light_state_variable & 0xff;
			controller_reply[CONTROLLER_VALUE2] = (light_state_variable >> 8) & 1;


			HiL_gateway_transmit_message(controller_reply[CONTROLLER_VALUE1],
										 controller_reply[CONTROLLER_VALUE2]);

				break;

			}



		default:
			// Reply with error
			controller_reply[CONTROLLER_VALUE1] = CONTROLLER_ERROR_NO_SUPPORT;
			HiL_gateway_transmit_message(0,32);
	}
}




