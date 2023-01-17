/*
 * HiL_callbacks.h
 *
 *  Created on: Dec 12, 2022
 *      Author: Olleblo
 *
 *      This file collect user defined callback functions. Callbacks are weakly defined in HAL-drivers.
 */

#ifndef INC_HIL_CALLBACKS_H_
#define INC_HIL_CALLBACKS_H_
#include "stm32f7xx_hal.h"
#include "HiL_config.h"
#include "cmsis_os.h"
#include "main.h"
#include <string.h>


//Executes duty cycle calculations.
void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim);

//Stores captured messages from UART.
void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size);

//Allows SPI RTOS task to run upon receiving a complete SPI transmission.
void HAL_SPI_RxCpltCallback(SPI_HandleTypeDef *hspi);

//Resets SPI to work properly after device under test has been reset.
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin);

#endif /* INC_HIL_CALLBACKS_H_ */
