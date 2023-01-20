*** Settings ***
Library           RobotFrameworkLib.py

*** Variables ***

*** Test Cases ***

Test Functionality 

	open server

	wait         200 milliseconds

	check if     TRAFFIC_LIGHTS are ALL_ON

	push         button3_center low for 100 milliseconds

	check_if     TRAFFIC_LIGHTS are ALL_ON

	push         button3_center low for 100 milliseconds

	wait         2 seconds

	check if     TRAFFIC_LIGHTS are ALL_ON

	push         button3_center low for 100 milliseconds

	wait         7 seconds

	check_if     TRAFFIC_LIGHTS are VERTICAL_YELLOW

	wait         3 seconds

	check_if     TRAFFIC_LIGHTS are ALL_RED

	wait         3 seconds

	check_if     TRAFFIC_LIGHTS are HORIZONTAL_YELLOW

	wait         3 seconds

	check_if     TRAFFIC_LIGHTS are HORIZONTAL_GREEN

	wait         10 seconds

	check_if     TRAFFIC_LIGHTS are HORIZONTAL_YELLOW

	wait         3 seconds

	check_if     TRAFFIC_LIGHTS are ALL_RED

	push         button3_center low for 100 milliseconds

	close server





	
