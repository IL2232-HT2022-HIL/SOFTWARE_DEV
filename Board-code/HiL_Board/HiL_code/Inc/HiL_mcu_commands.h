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


int HiL_mcu_commands_potentiometer_emulator(int value1, int value2);

int HiL_mcu_commands_binary_action (int binary_object, int desired_state);

int HiL_mcu_commands_binary_status (int binary_object);


#endif /* USER_COMMANDS_H_ */
