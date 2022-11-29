/*
 * HiL_Init_MSGQ.c
 *
 *  Created on: Nov 25, 2022
 *      Author: Olle
 */

#include "HiL_Init_MSGQ.h"

extern osMessageQueueId_t USB_MSGQ_Rx;
extern osMessageQueueId_t USB_MSGQ_Tx;

int HiL_Init_MSGQ (void) {

	USB_MSGQ_Rx = osMessageQueueNew(10, sizeof(MSGQ_obj), NULL);
  if (USB_MSGQ_Rx == NULL) {
	  return -1;
  }
  USB_MSGQ_Tx = osMessageQueueNew(10, sizeof(MSGQ_obj), NULL);
    if (USB_MSGQ_Tx == NULL) {
  	  return -1;
    }
  return 0;
}