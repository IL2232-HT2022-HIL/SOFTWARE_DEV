#from HiL_config import BINARY_OBJECTS, TIME_UNITS
import HiL_config
def HiL_client_communication_encode(instruction):
    string_list = instruction.split(" ")
    print(string_list)
    encoded_list = []
    encoded_list.append(HiL_config.CHANGE_REQUEST[string_list[0]])
    #print(encoded_list)
    if encoded_list[0] == 0: 
    #Original Format: ACTUATE [BINARY_OBJECTS] [BINARY_VALUE]
    #Encoded Format:  [0,_,_,0]
        encoded_list.append(HiL_config.BINARY_OBJECTS[string_list[1]])
        encoded_list.append(HiL_config.BINARY_VALUE[string_list[2]])
        encoded_list.append(0)
        return(encoded_list)
    elif encoded_list[0] == 1:
    #Format: POTEN POT [value for potentiometer]
    #Encoded Format:  [1,0,_,_]
        encoded_list.append(0)
        '''function of value transformation for POTEN should be added here'''
        encoded_list.append(string_list[2])
        encoded_list.append(0)
        return(encoded_list)
    elif encoded_list[0] == 2:
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

# The following codes are just for debuging this file
if __name__=="__main__":
    #push_instruction("button3_A for 3 seconds")
    #message = HiL_client_communication_encode("ACTUATE SW8 ON")
    #message = HiL_client_communication_encode("POTEN POT 2.8")
    message = HiL_client_communication_encode("SHT20 TEMP_SENSOR 37.8")
    print(message)
	#set_humi_instruction("HUMI_SENSOR to 44.5")
