#include "setup.h"

uint8_t aTxBuffer[3];

uint8_t aRxBuffer[4];



CRC_HandleTypeDef hcrc;


void init_i2c_buffer(){
	aRxBuffer[0]=0x00;
	aRxBuffer[1]=0x00;
	aRxBuffer[2]=0x00;
	aRxBuffer[3]=0x00;
	aTxBuffer[0]=0x00;
	aTxBuffer[1]=0x00;
	aTxBuffer[2]=0x00;
}

void init_i2c_listen(){
	if(HAL_I2C_EnableListen_IT(&hi2c1) != HAL_OK)
	    {
	      /* Transfer error in reception process */
	      Error_Handler();
	    }
}
