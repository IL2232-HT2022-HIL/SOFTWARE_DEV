

#define Temperature 1
#define Humidity 0

#define Max_hum 100
#define Min_hum 0

#define Max_temp 124.42
#define Min_temp -39.43


unsigned short temperature;
unsigned short humidity;


int HiL_mcu_commands_SHT20_control(int state_selection, double desired_state_value){
	if(state_selection == Humidity){
		if(desired_state_value < Min_hum && desired_state_value > Max_hum){
			return 3;
		}
		double hum = desired_state_value / 0.04;
		humidity = hum;

	}
	else if(state_selection == Temperature){
		if(desired_state_value < Min_temp && desired_state_value > Max_temp){
			return 3;
		}
		double temp = (desired_state_value + Min_temp) / 0.01;
		temperature = temp;
	}
	else {
		return 2;
	}
	return 0;
}
