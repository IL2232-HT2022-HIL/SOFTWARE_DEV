#from HiL_config import BINARY_OBJECTS, TIME_UNITS
import HiL_config
from HiL_config import ADC_RESOLUTION, DAC_RESOLUTION, DAC_REFERENCE, ADC_REFERENCE
def HiL_client_communication_encode(instruction):
    string_list = instruction.split(" ")
    print(string_list)
    encoded_list = []
    encoded_list.append(HiL_config.CHANGE_REQUEST[string_list[0]])
    #print(encoded_list)
    if encoded_list[0] == HiL_config.CHANGE_REQUEST["ACTUATE"]: 
    #Original Format: ACTUATE [BINARY_OBJECTS] [BINARY_VALUE]
    #Encoded Format:  [0,_,_,0]
        encoded_list.append(HiL_config.BINARY_OBJECTS[string_list[1]])
        encoded_list.append(HiL_config.BINARY_VALUE[string_list[2]])
        encoded_list.append(0)
        return(encoded_list)
    elif encoded_list[0] == HiL_config.CHANGE_REQUEST["POTEN"]:
    #Format: POTEN POT [value for potentiometer]
    #Encoded Format:  [1,0,_,_]
        encoded_list.append(0)
        '''function of value transformation for POTEN should be added here'''
        returned_list = HiL_client_POTEN_ADC(string_list[2])
        encoded_list.append(returned_list[0])
        encoded_list.append(returned_list[1])
        #encoded_list.append(string_list[2])
        #encoded_list.append(0)
        return(encoded_list)
    elif encoded_list[0] == HiL_config.CHANGE_REQUEST["SHT20"]:
    #Format: SHT20 [SHT20_OBJECTS] [value for object]
    #Encoded Format:  [2,_,_,_]
        encoded_list.append(HiL_config.SHT20_OBJECTS[string_list[1]])
        #the object is TEMP_SENSOR
        if encoded_list[1] == 0:
            '''function of value transformation for TEMP_SENSOR should be added here''' 
            encoded_list.append(string_list[2])
            encoded_list.append(0)
            return(encoded_list)
        #the object is HUMI_SENSOR
        elif encoded_list[1] == 1:
            '''function of value transformation for HUMI_SENSOR should be added here''' 
            encoded_list.append(string_list[2])
            encoded_list.append(0)
            return(encoded_list)
        else:
            raise Exception("Object is not supported, should be TEMP_SENSOR or HUMI_SENSOR")
    else: 
        raise Exception("Instruction is not supported. Please check the user guide.")

def HiL_client_communication_transmit(instruction):
    pass

def HiL_client_communication_receive(instruction):
    pass

def HiL_client_communication_decode(instruction):
    pass
def HiL_client_POTEN_ADC(decimal_string):
    decimal_value = float(decimal_string)
    bit_value = round(2**ADC_RESOLUTION*(decimal_value)/ADC_REFERENCE)
    print("Your value will be rounded.")
    print(bit_value)
    int_upper = (bit_value >> 8) & 0xff
    int_lower = bit_value & 0xff
	#print([int_lower,int_upper])
    return [int_lower,int_upper]

# The following codes are just for debuging this file
if __name__=="__main__":
    message = HiL_client_communication_encode("ACTUATE SW8 ON")
    #message = HiL_client_communication_encode("ACTUATE SW8 ON")
    #message = HiL_client_communication_encode("POTEN POT 2.8")
    #message = HiL_client_communication_encode("SHT20 TEMP_SENSOR 37.8")
    print(message)
	#set_humi_instruction("HUMI_SENSOR to 44.5")