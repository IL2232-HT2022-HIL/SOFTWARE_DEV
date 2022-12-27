/*
 * HiL_callbacks.h
 *
 *  Created on: Dec 12, 2022
 *      Author: Olleblo
 *
 *      This file contains the callback functions in use for the HiL-code
 */

#ifndef INC_HIL_CALLBACKS_H_
#define INC_HIL_CALLBACKS_H_
#include "stm32f7xx_hal.h"
#include "HiL_config.h"
#include "cmsis_os.h"
#include "main.h"
#include <string.h>


void HAL_TIM_IC_CaptureCallback(TIM_HandleTypeDef *htim);

void HAL_UARTEx_RxEventCallback(UART_HandleTypeDef *huart, uint16_t Size);

void HAL_SPI_RxCpltCallback(SPI_HandleTypeDef *hspi);

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin);

#endif /* INC_HIL_CALLBACKS_H_ */
