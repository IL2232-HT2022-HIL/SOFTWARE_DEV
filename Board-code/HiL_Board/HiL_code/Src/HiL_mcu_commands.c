/*
 * user_commands.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger Stenberg
 */


#include "HiL_mcu_commands.h"
#include "cmsis_os.h"


extern uint8_t Duty;
extern TIM_HandleTypeDef htim1;


extern uint8_t uart_main_buffer[HIL_UART_BUFFER_SIZE];
uint8_t uart_main_buffer_pointer = 0;



uint8_t HiL_mcu_commands_potentiometer_emulator(uint8_t value1, uint8_t value2)
{

	uint16_t desired_output_voltage = value1 + (value2 << 8);

	if( (desired_output_voltage < 0) || (desired_output_voltage > 4095) ){
		return 3; //error: out of bounds
	}

	HAL_DAC_SetValue(&hdac, DAC_CHANNEL_1, DAC_ALIGN_12B_R, desired_output_voltage);
	return 0;
}


uint8_t HiL_mcu_commands_binary_action (uint8_t binary_object, uint8_t desired_state)
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

uint8_t HiL_mcu_commands_binary_status (uint8_t binary_object)
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

uint8_t HiL_mcu_commands_PWM_measure ()
{
													// Start timers and interrupts
		HAL_TIM_IC_Start_IT(&htim1, TIM_CHANNEL_1); // Primary channel - rising edge - rinse and repeat
		HAL_TIM_IC_Start(&htim1, TIM_CHANNEL_2);    // Secondary channel - falling edge - stop second counter

		osDelay(1);				//	Wait for  pwm-period to complete. Smallest tick time is currently 1 millisecond. PWM freq is 8 kHz, so this is slow enough.

												   // Stop timers and interrupts
		HAL_TIM_IC_Stop_IT(&htim1, TIM_CHANNEL_1); // Primary channel - rising edge - rinse and repeat
		HAL_TIM_IC_Stop(&htim1, TIM_CHANNEL_2);    // Secondary channel - falling edge - stop second counter

		return Duty;
}


uint16_t HiL_mcu_commands_UART_handler (uint8_t controller_get_action)
{
	if (controller_get_action == 0)
	{
		uart_main_buffer_pointer = 0;
		return 0<<12; // transaction status: all good
	}
	else
	{
		uint16_t return_value = uart_main_buffer[uart_main_buffer_pointer];

		if (return_value != 0)
		{
			uart_main_buffer_pointer = (uart_main_buffer_pointer < HIL_UART_BUFFER_SIZE ? uart_main_buffer_pointer+1 : 0);
		}

		return return_value;
	}

}


