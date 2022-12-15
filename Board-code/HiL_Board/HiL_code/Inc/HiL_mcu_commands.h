/*
 * user_commands.h
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger Stenberg
 */

#ifndef USER_COMMANDS_H_
#define USER_COMMANDS_H_


#include "main.h"
#include "HiL_config.h"
#include <stdio.h>


extern DAC_HandleTypeDef hdac;


uint8_t HiL_mcu_commands_potentiometer_emulator(uint8_t value1, uint8_t value2);

uint8_t HiL_mcu_commands_binary_action (uint8_t binary_object, uint8_t desired_state);

uint8_t HiL_mcu_commands_binary_status (uint8_t binary_object);

uint8_t HiL_mcu_commands_PWM_measure ();

uint16_t HiL_mcu_commands_UART_handler (uint8_t controller_get_action);


#endif /* USER_COMMANDS_H_ */
