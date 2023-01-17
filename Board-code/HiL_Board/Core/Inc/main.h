/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32f7xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define HiL_Disp_Data_Instr_Pin GPIO_PIN_3
#define HiL_Disp_Data_Instr_GPIO_Port GPIOE
#define HiL_595_Reset_Pin GPIO_PIN_15
#define HiL_595_Reset_GPIO_Port GPIOC
#define HiL_595_Reset_EXTI_IRQn EXTI15_10_IRQn
#define HiL_TL2_Car_Pin GPIO_PIN_7
#define HiL_TL2_Car_GPIO_Port GPIOF
#define HiL_Disp_Reset_Pin GPIO_PIN_0
#define HiL_Disp_Reset_GPIO_Port GPIOC
#define HiL_595_STCP_Pin GPIO_PIN_2
#define HiL_595_STCP_GPIO_Port GPIOC
#define HiL_USR_LED1_Pin GPIO_PIN_0
#define HiL_USR_LED1_GPIO_Port GPIOA
#define HiL_Poti_Pin GPIO_PIN_4
#define HiL_Poti_GPIO_Port GPIOA
#define HiL_USR_LED2_Pin GPIO_PIN_0
#define HiL_USR_LED2_GPIO_Port GPIOB
#define HiL_SPI3_MOSI_Pin GPIO_PIN_2
#define HiL_SPI3_MOSI_GPIO_Port GPIOB
#define HiL_UART7_RX_Pin GPIO_PIN_7
#define HiL_UART7_RX_GPIO_Port GPIOE
#define HiL_UART7_TX_Pin GPIO_PIN_8
#define HiL_UART7_TX_GPIO_Port GPIOE
#define HiL_595_Enable_Pin GPIO_PIN_9
#define HiL_595_Enable_GPIO_Port GPIOE
#define HiL_Disp_CS_Pin GPIO_PIN_12
#define HiL_Disp_CS_GPIO_Port GPIOE
#define HiL_SW5_Pin GPIO_PIN_10
#define HiL_SW5_GPIO_Port GPIOB
#define HiL_SW8_Pin GPIO_PIN_14
#define HiL_SW8_GPIO_Port GPIOB
#define HiL_SW6_Pin GPIO_PIN_15
#define HiL_SW6_GPIO_Port GPIOB
#define HiL_button3_B_Pin GPIO_PIN_2
#define HiL_button3_B_GPIO_Port GPIOG
#define HiL_button3_A_Pin GPIO_PIN_3
#define HiL_button3_A_GPIO_Port GPIOG
#define HiL_LIS2DW12TR_Int1_Pin GPIO_PIN_10
#define HiL_LIS2DW12TR_Int1_GPIO_Port GPIOA
#define TMS_Pin GPIO_PIN_13
#define TMS_GPIO_Port GPIOA
#define TCK_Pin GPIO_PIN_14
#define TCK_GPIO_Port GPIOA
#define HiL_TL3_Car_Pin GPIO_PIN_15
#define HiL_TL3_Car_GPIO_Port GPIOA
#define HiL_SPI3_SCK_Pin GPIO_PIN_10
#define HiL_SPI3_SCK_GPIO_Port GPIOC
#define HiL_TL1_Car_Pin GPIO_PIN_12
#define HiL_TL1_Car_GPIO_Port GPIOC
#define HiL_CAN1_RX_Pin GPIO_PIN_0
#define HiL_CAN1_RX_GPIO_Port GPIOD
#define HiL_CAN1_TX_Pin GPIO_PIN_1
#define HiL_CAN1_TX_GPIO_Port GPIOD
#define HiL_TL4_Car_Pin GPIO_PIN_2
#define HiL_TL4_Car_GPIO_Port GPIOD
#define HiL_button3_C_Pin GPIO_PIN_4
#define HiL_button3_C_GPIO_Port GPIOD
#define HiL_button3_D_Pin GPIO_PIN_5
#define HiL_button3_D_GPIO_Port GPIOD
#define HiL_button3_center_Pin GPIO_PIN_6
#define HiL_button3_center_GPIO_Port GPIOD
#define HiL_595_DS_Pin GPIO_PIN_7
#define HiL_595_DS_GPIO_Port GPIOD
#define HiL_595_SHCP_Pin GPIO_PIN_3
#define HiL_595_SHCP_GPIO_Port GPIOB
#define HiL_SW7_Pin GPIO_PIN_4
#define HiL_SW7_GPIO_Port GPIOB
#define HiL_LIS2DW12TR_Int2_Pin GPIO_PIN_5
#define HiL_LIS2DW12TR_Int2_GPIO_Port GPIOB
#define LD2_Pin GPIO_PIN_7
#define LD2_GPIO_Port GPIOB
#define HiL_I2C1_SCL_Pin GPIO_PIN_8
#define HiL_I2C1_SCL_GPIO_Port GPIOB
#define HiL_I2C1_SDA_Pin GPIO_PIN_9
#define HiL_I2C1_SDA_GPIO_Port GPIOB
/* USER CODE BEGIN Private defines */

/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
