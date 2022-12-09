#include "cmsis_os2.h"

typedef struct {                                // object data type
  uint8_t Buf[32];
} MSGQ_obj;

osMessageQueueId_t UART_get_Q;
osMessageQueueId_t UART_send_Q;

int Init_MsgQueue (osMessageQueueId_t Q_name);
