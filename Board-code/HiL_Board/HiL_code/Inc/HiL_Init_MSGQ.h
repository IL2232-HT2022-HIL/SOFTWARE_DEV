/*
 * HiL_Init_MSGQ.h
 *
 *  Created on: Nov 25, 2022
 *      Author: Olle
 *
 *      This file contains the initialization for the message queues in use in freeRTOS
 *
 */

#ifndef INC_HIL_INIT_MSGQ_H_
#define INC_HIL_INIT_MSGQ_H_

#define HiL_USB_MSQG_len 10

#include "main.h"
#include "cmsis_os.h"
#include "HiL_MSGQ_obj.h"


int HiL_Init_MSGQ();



#endif /* INC_HIL_INIT_MSGQ_H_ */
