/*
 * _gateway.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */


#include "HiL_gateway.h"


void HiL_gateway_transmit_message(int value1, int value2)
{
	uint8_t values[2];
	values[0] = value1;
	values[1] = value2;


	CDC_Transmit_FS( /*(uint8_t *)*/ values, sizeof(values));		// Transmit what's been recieved in our msg queue
}
