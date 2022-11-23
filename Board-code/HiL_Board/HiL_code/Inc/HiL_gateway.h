/*
 * _gateway.h
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */

#ifndef GATEWAY__GATEWAY_H_
#define GATEWAY__GATEWAY_H_

#include "main.h"
#include "HiL_config.h"
#include <stdio.h>


int *  HiL_gateway_get_message();

void   HiL_gateway_transmit_message(int value1, int value2);


#endif /* GATEWAY__GATEWAY_H_ */
