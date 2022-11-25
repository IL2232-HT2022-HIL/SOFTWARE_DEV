/*
 * HiL_MSGQ_obj.h
 *
 *  Created on: Nov 25, 2022
 *      Author: Olle
 */

#ifndef INC_HIL_MSGQ_OBJ_H_
#define INC_HIL_MSGQ_OBJ_H_

typedef struct {                                // Object data type
  uint8_t Buf[4];
  //uint8_t Idx;
} MSGQ_obj;

#endif /* INC_HIL_MSGQ_OBJ_H_ */
