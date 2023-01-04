/*
 * HiL_callbacks.c
 *
 *  Created on: Dec 12, 2022
 *      Author: Olleblo
 *
 *      This file collect user defined callback functions. Callbacks are weakly defined in HAL-drivers.
 *
 *
 */

#include "HiL_callbacks.h"


uint32_t Cnt_full = 0;
uint32_t Cnt_high = 0;							// Variables for HAL_TIM_IC_CaptureCallback()
uint8_t Duty = 0;


uint8_t uart_main_buffer[HIL_UART_BUFFER_SIZE] = "Default";
extern uint8_t uart_rx_buffer[HIL_UART_BUFFER_SIZE];
extern UART_HandleTypeDef huart7;
extern uint8_t temp_light_state[3];
extern osSemaphoreId_t LightOnSemHandle;
extern SPI_HandleTypeDef hspi1;
extern void MX_SPI1_Init();



void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim) {						// Timer callback code on interrupts from rising and falling edges
	if (htim->Instance == TIM1) {
		// Used for duty cycle measurements

		//#define TIMER_CLOCK_FREQ 96000000 // APB2 Timer Clock. With 96 MHz, 16 bit res -> Reload/wraparound freq @ 732 Hz
																				// -> Tested lowest measureable pwm freq is 1.7 kHz

		Cnt_full = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_1) + 1;
		Cnt_high = HAL_TIM_ReadCapturedValue(htim, TIM_CHANNEL_2);

		Duty =  100 * Cnt_high / Cnt_full;
	}
}

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size)
{
	if (huart->Instance == UART7)
	{
		memcpy(uart_main_buffer,uart_rx_buffer,Size);
		HAL_UARTEx_ReceiveToIdle_DMA(&huart7, uart_rx_buffer, HIL_UART_BUFFER_SIZE);
	}

}

void HAL_SPI_RxCpltCallback(SPI_HandleTypeDef *hspi){
	//printf("hello from spi complete\n\r");
	//printf("error %ld\n\r", hspi->ErrorCode);
	osSemaphoreRelease(LightOnSemHandle);

}

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin){
	//Used to handle reset of the MCU board that is being tested. Without it, bit shift occurs in SPI-communication.


	if(GPIO_Pin & HiL_595_Reset_Pin){

//		HAL_StatusTypeDef status;

		HAL_SPI_DMAStop(&hspi1);

		__HAL_RCC_SPI1_FORCE_RESET();
		__HAL_RCC_SPI1_RELEASE_RESET();

		MX_SPI1_Init();			//Requires that function declaration in main is NOT static!
		/*status =*/ HAL_SPI_Receive_DMA(&hspi1, temp_light_state, sizeof(temp_light_state));

	}
}
