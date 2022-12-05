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
#include "usbd_cdc_if.h" //for transmission over USB


void HiL_gateway_transmit_message(uint8_t value1, uint8_t value2);


#endif /* GATEWAY__GATEWAY_H_ */
