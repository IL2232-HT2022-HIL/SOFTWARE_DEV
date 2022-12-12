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
uint32_t Cnt_high = 0;															// Variables for HAL_TIM_IC_CaptureCallback()
uint8_t Duty = 0;


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
