
from HiL_config import CONTROLLER_REQUEST, CONTROLLER_OBJECTS, CONTROLLER_ACTIONS #FOR ENCODING
from HiL_config import COM_PORT, USB_BAUD_RATE                                    #FOR USB

import time
import serial


def HiL_client_communication_serial_port(enable):


    if (enable):

        try:
            global HiL_serial_link
            HiL_serial_link = serial.Serial(COM_PORT, USB_BAUD_RATE, timeout=0.5)
            if HiL_serial_link.isOpen():
                print("serial port opened")
            
        except Exception as exc:
            raise

    else:
        
        try:
            HiL_serial_link.close()
            if not HiL_serial_link.isOpen():
                print("Serial port is closed")
        
        except Exception as exc:
            raise

# send messages
def HiL_client_communication_transmit(encoded_message):
    
    try:
        HiL_serial_link.reset_input_buffer()
        HiL_serial_link.write(bytes(encoded_message))
        
    except Exception as exc:
        raise

# receive messages
def HiL_client_communication_receive():
    
    try:
        recieved_message_array = list(HiL_serial_link.read(HiL_serial_link.in_waiting))
        return recieved_message_array[0:2:]
        
    except Exception as exc:
        raise


def HiL_client_communication_encode(message):
    
    string_list = message.split(" ")
    
    controller_request = CONTROLLER_REQUEST[string_list[0]]
    controller_object  = CONTROLLER_OBJECTS[string_list[1]].object_value

    if   string_list[2] in CONTROLLER_ACTIONS:
        controller_action1 = CONTROLLER_ACTIONS[string_list[2]]

    elif string_list[2] in CONTROLLER_OBJECTS:
        controller_action1 = CONTROLLER_OBJECTS[string_list[2]].object_value

    else:
        controller_action1 = int(string_list[2])

    if len(string_list) != 4:  # in case last byte not used
        controller_action2 = 0 # dummy byte
    
    elif string_list[3] in CONTROLLER_ACTIONS:
        controller_action2 = CONTROLLER_ACTIONS[string_list[3]]
    
    else:
        controller_action2 = int(string_list[3])
    
    return [controller_request, controller_object, controller_action1, controller_action2]


def HiL_client_communication_decode(recieved_message_array):

    value1 = recieved_message_array[0] #LSB
    value2 = recieved_message_array[1] #MSB

    return (value2 << 8) + value1


if __name__ == '__main__':
    pass
        


