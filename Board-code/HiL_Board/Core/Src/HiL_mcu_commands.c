//#include "main.h"
#include "setup.h"

/* USER CODE BEGIN Includes */
#define COUNTOF(__BUFFER__)   (sizeof(__BUFFER__) / sizeof(*(__BUFFER__)))
/* Size of Transmission buffer */
#define TXBUFFERSIZE                      (COUNTOF(aTxBuffer))
/* Size of Reception buffer */
#define RXBUFFERSIZE                      TXBUFFERSIZE
/* USER CODE END Includes */

__IO uint32_t     Transfer_Direction = 0;
__IO uint32_t     Xfer_Complete = 0;



#define Temperature 1
#define Humidity 0

#define Max_hum 100
#define Min_hum 0

#define Max_temp 124.42
#define Min_temp -39.43

#define send_temp_h 0xE3
#define send_temp_nh 0xF3
#define send_hum_h 0xE5
#define send_hum_nh 0xF5


unsigned short temperature;
unsigned short humidity;



int HiL_mcu_commands_SHT20_control(int state_selection, double desired_state_value){
	if(state_selection == Humidity){
		if(desired_state_value < Min_hum && desired_state_value > Max_hum){
			return 3;
		}
		double hum = desired_state_value / 0.04;
		humidity = hum;
		humidity = (humidity<<4)+2;

	}
	else if(state_selection == Temperature){
		if(desired_state_value < Min_temp && desired_state_value > Max_temp){
			return 3;
		}
		double temp = (desired_state_value + Min_temp) / 0.01;
		temperature = temp;
		temperature = (temperature<<2)+2;
	}
	else {
		return 2;
	}
	return 0;
}


int crc(int input){
	return 0;
}


/**
  * @brief  Tx Transfer completed callback.
  * @param  I2cHandle: I2C handle.
  * @note   This example shows a simple way to report end of IT Tx transfer, and
  *         you can add your own implementation.
  * @retval None
  */

void HAL_I2C_SlaveTxCpltCallback(I2C_HandleTypeDef *I2cHandle)
{
  /* Toggle LED4: Transfer in transmission process is correct */

  Xfer_Complete = 1;

}


/**
  * @brief  Rx Transfer completed callback.
  * @param  I2cHandle: I2C handle
  * @note   This example shows a simple way to report end of IT Rx transfer, and
  *         you can add your own implementation.
  * @retval None
  */
void HAL_I2C_SlaveRxCpltCallback(I2C_HandleTypeDef *I2cHandle)
{
  /* Toggle LED4: Transfer in reception process is correct */

  Xfer_Complete = 1;
  if (aRxBuffer[1] == send_temp_h || aRxBuffer[1] == send_temp_nh){
	  int temp = temperature<<8;
	  temp = crc(temp);
	  aTxBuffer[0] = (temp >> 16) & 0xFF;
	  aTxBuffer[1] = (temp >> 8) & 0xFF;
	  aTxBuffer[2] = (temp >> 0) & 0xFF;
  }
  else if (aRxBuffer[1] == send_hum_h || aRxBuffer[1] == send_hum_nh){
	  int hum = humidity<<8;
	  hum = crc(hum);
	  aTxBuffer[0] = (hum >> 16) & 0xFF;
	  aTxBuffer[1] = (hum >> 8) & 0xFF;
	  aTxBuffer[2] = (hum >> 0) & 0xFF;
  }
  aRxBuffer[0]=0x00;
  aRxBuffer[1]=0x00;
  aRxBuffer[2]=0x00;
  aRxBuffer[3]=0x00;
}



/**
  * @brief  Slave Address Match callback.
  * @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
  *                the configuration information for the specified I2C.
  * @param  TransferDirection: Master request Transfer Direction (Write/Read), value of @ref I2C_XferOptions_definition
  * @param  AddrMatchCode: Address Match Code
  * @retval None
  */
void HAL_I2C_AddrCallback(I2C_HandleTypeDef *hi2c, uint8_t TransferDirection, uint16_t AddrMatchCode)
{
  Transfer_Direction = TransferDirection;
  if (Transfer_Direction != 0)
  {
     /*##- Start the transmission process #####################################*/
  /* While the I2C in reception process, user can transmit data through
     "aTxBuffer" buffer */
  if (HAL_I2C_Slave_Seq_Transmit_IT(&hi2c1, (uint8_t *)aTxBuffer, TXBUFFERSIZE, I2C_FIRST_AND_LAST_FRAME) != HAL_OK)

    {
    /* Transfer error in transmission process */
    Error_Handler();
  }

  }
  else
  {

      /*##- Put I2C peripheral in reception process ###########################*/
  if (HAL_I2C_Slave_Seq_Receive_IT(&hi2c1, (uint8_t *)aRxBuffer, RXBUFFERSIZE, I2C_FIRST_AND_LAST_FRAME) != HAL_OK)
    {
    /* Transfer error in reception process */
    Error_Handler();
  }

  }

}

/**
  * @brief  Listen Complete callback.
  * @param  hi2c Pointer to a I2C_HandleTypeDef structure that contains
  *                the configuration information for the specified I2C.
  * @retval None
  */
void HAL_I2C_ListenCpltCallback(I2C_HandleTypeDef *hi2c)
{
}

/**
  * @brief  I2C error callbacks.
  * @param  I2cHandle: I2C handle
  * @note   This example shows a simple way to report transfer error, and you can
  *         add your own implementation.
  * @retval None
  */
void HAL_I2C_ErrorCallback(I2C_HandleTypeDef *I2cHandle)
{
  /** Error_Handler() function is called when error occurs.
    * 1- When Slave doesn't acknowledge its address, Master restarts communication.
    * 2- When Master doesn't acknowledge the last data transferred, Slave doesn't care in this example.
    */
  if (HAL_I2C_GetError(I2cHandle) != HAL_I2C_ERROR_AF)
  {
    Error_Handler();
  }
}