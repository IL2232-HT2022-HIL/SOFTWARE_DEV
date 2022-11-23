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


int HiL_mcu_commands_potentiometer_emulator(int desired_output_voltage);

int HiL_mcu_commands_binary_action (int binary_object, int desired_state);

int HiL_mcu_commands_binary_status (int binary_object);


#endif /* USER_COMMANDS_H_ */
