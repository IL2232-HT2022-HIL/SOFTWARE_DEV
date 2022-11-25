/*
 * _controller.h
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 *
 *
 *      This file contains the functions needed for controlling the HiL board.
 *      It is written in a way that would allow a designer to either choose data coming from
 *      Ethernet or any other peripheral, such as SPI or USB.
 *
 *
 *
 *
 */


#ifndef CONTROLLER__CONTROLLER_H_
#define CONTROLLER__CONTROLLER_H_

#include "main.h"
#include "HiL_config.h"
#include <stdio.h>

#include "HiL_gateway.h"
#include "HiL_mcu_commands.h"

//parses message, and tries to execute commands.
void HiL_controller_read_message(int* recieved_data);

// Function send message to gateway
void HiL_controller_send_message();

// get the pointer to the recieved client message
void HiL_controller_copy_array(int* to_be_copied);

#endif /* CONTROLLER__CONTROLLER_H_ */
