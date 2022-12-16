#include "main.h"


/* Buffer used for transmission */
extern uint8_t aTxBuffer[3];

/* Buffer used for reception */
extern uint8_t aRxBuffer[4];


extern I2C_HandleTypeDef hi2c1;

extern CRC_HandleTypeDef hcrc;


void init_i2c_buffer();
void init_i2c_listen();
