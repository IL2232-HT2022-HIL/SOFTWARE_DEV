/*
 * user_commands.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger Stenberg
 */


#include "HiL_mcu_commands.h"


int HiL_mcu_commands_binary_action (int binary_object, int desired_state)
{

	GPIO_PinState pin_state;
	
	if (desired_state == ON)
	{
		pin_state = GPIO_PIN_SET;
	}
	else if (desired_state == OFF)
	{
		pin_state = GPIO_PIN_RESET;
	}
	else
	{
		return CONTROLLER_ERROR_BAD_REQUEST; // Invalid state indication
	}

	switch (binary_object)
	{

		case HiL_SW5:
			HAL_GPIO_WritePin(HiL_SW5_GPIO_Port, HiL_SW5_Pin, pin_state);
			break;

		case HiL_SW6:
			HAL_GPIO_WritePin(HiL_SW6_GPIO_Port, HiL_SW6_Pin, pin_state);
			break;

		case HiL_SW7:
			HAL_GPIO_WritePin(HiL_SW7_GPIO_Port, HiL_SW7_Pin, pin_state);
			break;

		case HiL_SW8:
			HAL_GPIO_WritePin(HiL_SW8_GPIO_Port, HiL_SW8_Pin, pin_state);
			break;

		case HiL_button3_A:
			HAL_GPIO_WritePin(HiL_button3_A_GPIO_Port, HiL_button3_A_Pin, pin_state);
			break;

		case HiL_button3_B:
			HAL_GPIO_WritePin(HiL_button3_B_GPIO_Port, HiL_button3_B_Pin, pin_state);
			break;

		case HiL_button3_C:
			HAL_GPIO_WritePin(HiL_button3_C_GPIO_Port, HiL_button3_C_Pin, pin_state);
			break;

		case HiL_button3_D:
			HAL_GPIO_WritePin(HiL_button3_D_GPIO_Port, HiL_button3_D_Pin, pin_state);
			break;

		case HiL_button3_center:
			HAL_GPIO_WritePin(HiL_button3_center_GPIO_Port, HiL_button3_center_Pin, pin_state);
			break;

		case HiL_TL1_Car:
			HAL_GPIO_WritePin(HiL_TL1_Car_GPIO_Port, HiL_TL1_Car_Pin, pin_state);
			break;

		case HiL_TL2_Car:
			HAL_GPIO_WritePin(HiL_TL2_Car_GPIO_Port, HiL_TL2_Car_Pin, pin_state);
			break;

		case HiL_TL3_Car:
			HAL_GPIO_WritePin(HiL_TL3_Car_GPIO_Port, HiL_TL3_Car_Pin, pin_state);
			break;

		case HiL_TL4_Car:
			HAL_GPIO_WritePin(HiL_TL4_Car_GPIO_Port, HiL_TL4_Car_Pin, pin_state);
			break;

		default:
			return CONTROLLER_ERROR_NO_SUPPORT; // Switch not currently supported

	}

	return 0; // Function returned successfully 
	
}

int HiL_mcu_commands_binary_status (int binary_object)
{
	switch (binary_object)
	{

		case HiL_SW5:
			return HAL_GPIO_ReadPin(HiL_SW5_GPIO_Port, HiL_SW5_Pin);

		case HiL_SW6:
			return HAL_GPIO_ReadPin(HiL_SW6_GPIO_Port, HiL_SW6_Pin);

		case HiL_SW7:
			return HAL_GPIO_ReadPin(HiL_SW7_GPIO_Port, HiL_SW7_Pin);

		case HiL_SW8:
			return HAL_GPIO_ReadPin(HiL_SW8_GPIO_Port, HiL_SW8_Pin);

		case HiL_button3_A:
			return HAL_GPIO_ReadPin(HiL_button3_A_GPIO_Port, HiL_button3_A_Pin);

		case HiL_button3_B:
			return HAL_GPIO_ReadPin(HiL_button3_B_GPIO_Port, HiL_button3_B_Pin);

		case HiL_button3_C:
			return HAL_GPIO_ReadPin(HiL_button3_C_GPIO_Port, HiL_button3_C_Pin);

		case HiL_button3_D:
			return HAL_GPIO_ReadPin(HiL_button3_D_GPIO_Port, HiL_button3_D_Pin);

		case HiL_button3_center:
			return HAL_GPIO_ReadPin(HiL_button3_center_GPIO_Port, HiL_button3_center_Pin);

		case HiL_TL1_Car:
			return HAL_GPIO_ReadPin(HiL_TL1_Car_GPIO_Port, HiL_TL1_Car_Pin);

		case HiL_TL2_Car:
			return HAL_GPIO_ReadPin(HiL_TL2_Car_GPIO_Port, HiL_TL2_Car_Pin);

		case HiL_TL3_Car:
			return HAL_GPIO_ReadPin(HiL_TL3_Car_GPIO_Port, HiL_TL3_Car_Pin);

		case HiL_TL4_Car:
			return HAL_GPIO_ReadPin(HiL_TL4_Car_GPIO_Port, HiL_TL4_Car_Pin);

		default:
			return CONTROLLER_ERROR_NO_SUPPORT; // Switch not currently supported

	}
}
