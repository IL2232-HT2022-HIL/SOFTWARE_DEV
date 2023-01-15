/*
 * HiL_gateway.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */


#include "HiL_gateway.h"

void HiL_gateway_transmit_message(uint8_t value1, uint8_t value2)
{
	uint8_t values[2];
	values[0] = value1;
	values[1] = value2;

	//Using USB communication:
	CDC_Transmit_FS(values, sizeof(values));		// Transmit what's been recieved in our msg queue
}
