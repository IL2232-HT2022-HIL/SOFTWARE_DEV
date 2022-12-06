/*
 * HiL_MSGQ_obj.h
 *
 *  Created on: Nov 25, 2022
 *      Author: Olle
 *
 *      This file contains the structure for message queue objects that are in use for usb communication
 *
 */

#ifndef INC_HIL_MSGQ_OBJ_H_
#define INC_HIL_MSGQ_OBJ_H_

#define HiL_MSGQ_Buf_arr_len 4					// Array length for each message

typedef struct {                                // Object data type
  uint8_t Buf[HiL_MSGQ_Buf_arr_len];
  //uint8_t Idx;
} MSGQ_obj;

#endif /* INC_HIL_MSGQ_OBJ_H_ */
