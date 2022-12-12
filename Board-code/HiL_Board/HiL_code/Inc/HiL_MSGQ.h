/*
 * HiL_MSGQ_obj.h
 *
 *  Created on: Nov 25, 2022
 *      Author: Olle
 *
 *      This file contains the structure for message queues and message queue objects that are in use for usb communication
 *
 */

#ifndef INC_HIL_MSGQ_H_
#define INC_HIL_MSGQ_H_

#include "cmsis_os.h"

#define HiL_USB_MSQG_len 10						// Message queue length for USB queues.

#define HiL_MSGQ_Buf_arr_len 4					// Array length for each message

typedef struct {                                // Message object data type
  uint8_t Buf[HiL_MSGQ_Buf_arr_len];
  //uint8_t Idx;
} MSGQ_obj;

uint8_t HiL_Init_MSGQ();						// Starts up the message queues in use.

#endif /* INC_HIL_MSGQ_H_ */
