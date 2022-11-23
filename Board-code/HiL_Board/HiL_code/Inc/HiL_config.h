/*
 * HiL_config.h
 *
 *  Created on: Oct 24, 2022
 *      Author: Holger
 */

#ifndef HIL_CONFIG_H_
#define HIL_CONFIG_H_

// FOR DEBUG
#define CONTROLLER_INFO 0

// -------------------------------------
// KEYWORDS FOR PARSING

// KEYWORDS FOR VALUE CHANGE MESSAGES
#define CONTROLLER_REQUEST 0
#define CONTROLLER_OBJECT  1
#define CONTROLLER_ACTION1 2
#define CONTROLLER_ACTION2 3

// FOR VALUE RECEIVE MESSAGES
#define CONTROLLER_GET_GROUP  1
#define CONTROLLER_GET_OBJECT 2

// FOR REPLY
#define CONTROLLER_VALUE1 0
#define CONTROLLER_VALUE2 1

// -------------------------------------
// CONTROLLER_REQUESTS

#define CONTROLLER_REQUEST_GET           0 // get data from server
#define CONTROLLER_REQUEST_ACTUATE       1 // button/switch stimuli
#define CONTROLLER_REQUEST_POTENTIOMETER 2 // potentiometer emulation
#define CONTROLLER_REQUEST_SHT20         3 // SHT20 emulator stimuli

// -------------------------------------
// GET GROUPS

#define CONTROLLER_GET_GROUP_BINARY 0

// -------------------------------------
// CONTROLLER_OBJECTS

// BINARY_OBJECTS
#define HiL_SW5            0
#define HiL_SW6            1
#define HiL_SW7            2
#define HiL_SW8            3
#define HiL_button3_A      4
#define HiL_button3_B      5
#define HiL_button3_C      6
#define HiL_button3_D      7
#define HiL_button3_center 8
#define HiL_TL1_Car        9
#define HiL_TL2_Car        10
#define HiL_TL3_Car        11
#define HiL_TL4_Car        12

// SHT20_OBJECTS
#define HiL_SHT20_TEMPERATURE 0 
#define HiL_SHT20_HUMIDITY    1 

// POTENTIOMETER OBJECTS
#define HiL_Poti 0

// -------------------------------------
// ACTIONS

#define OFF 0
#define ON  1
#define GPIO_PIN_RESET 0
#define GPIO_PIN_SET   1

// -------------------------------------
// ERROR CODES

#define CONTROLLER_ERROR_UNSPECIFIED 1
#define CONTROLLER_ERROR_NO_SUPPORT  2
#define CONTROLLER_ERROR_BAD_REQUEST 3


#endif /* HIL_CONFIG_H_ */
