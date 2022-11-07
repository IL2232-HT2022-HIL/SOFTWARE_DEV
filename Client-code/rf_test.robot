*** Settings ***
Library           RobotFrameworkLib.py

*** Variables ***

*** Test Cases ***

Test Button Functionality 

	run status
	turn on    button3_A
	turn off   button3_A
	push    button3_A for 3 seconds
	set temp    TEMP_SENSOR to 35
	Set Humi    HUMI_SENSOR to 45.7
