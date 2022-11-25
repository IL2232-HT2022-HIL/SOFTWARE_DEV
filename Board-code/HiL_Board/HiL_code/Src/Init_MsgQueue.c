/*
 * Init_MsgQueue.c
 *
 *  Created on: Nov 25, 2022
 *      Author: olleb
 */


int Init_MsgQueue (void) {

  MSGQ_Rx = osMessageQueueNew(10, sizeof(MSGQ_obj), NULL);
  if (MSGQ_Rx == NULL) {
	  return -1;
  }
  MSGQ_Tx = osMessageQueueNew(10, sizeof(MSGQ_obj), NULL);
    if (MSGQ_Tx == NULL) {
  	  return -1;
    }
  return 0;
}
