/*
 * HiL_MSGQ.c
 *
 *  Created on: Dec 12, 2022
 *      Author: OlleBlo
 *
 *      This file contains the initialization for the message queues and other message queue related functions in use in freeRTOS
 */


#include "HiL_MSGQ.h"

extern osMessageQueueId_t USB_MSGQ_Rx;
//extern osMessageQueueId_t USB_MSGQ_Tx;

uint8_t HiL_Init_MSGQ (void) {

	USB_MSGQ_Rx = osMessageQueueNew(HiL_USB_MSQG_len, sizeof(MSGQ_obj), NULL);
  if (USB_MSGQ_Rx == NULL) {
	  return -1;
  }
//  USB_MSGQ_Tx = osMessageQueueNew(10, sizeof(MSGQ_obj), NULL);
//    if (USB_MSGQ_Tx == NULL) {
//  	  return -1;
//    }
  return 0;
}
