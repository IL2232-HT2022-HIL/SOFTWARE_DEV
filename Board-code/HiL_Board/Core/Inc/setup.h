#include "main.h"


/* Buffer used for transmission */
uint8_t aTxBuffer[3];

/* Buffer used for reception */
uint8_t aRxBuffer[4];


I2C_HandleTypeDef hi2c1;


void init_i2c_buffer();
void init_i2c_listen();
