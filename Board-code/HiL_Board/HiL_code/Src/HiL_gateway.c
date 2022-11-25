/*
 * _gateway.c
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */


#include "HiL_gateway.h"


int emulated_message[256] = {CONTROLLER_REQUEST_POTENTIOMETER, HiL_Poti, 0, 0};

int *  HiL_gateway_get_message()
{	
	return emulated_message;
}

void HiL_gateway_transmit_message(int value1, int value2)
{
	printf("[%i,%i]\n", value1, value2);

}
