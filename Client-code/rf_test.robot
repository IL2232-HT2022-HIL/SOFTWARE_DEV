*** Settings ***
Library           RobotFrameworkLib.py

*** Variables ***

*** Test Cases ***

Test Button Functionality 

	open server
	turn on     TL1_Car
	check if    TL1_Car is 1
	turn off    TL1_Car
	check if    TL1_Car is 0
	tune    Poti to 2.3

	close server
	
	
