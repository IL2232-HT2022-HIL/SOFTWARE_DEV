
from HiL_config import CONTROLLER_REQUEST, CONTROLLER_OBJECTS, CONTROLLER_ACTIONS #FOR ENCODING
from HiL_config import COM_PORT, USB_BAUD_RATE, VIRTUAL_SERVER    #FOR USB

import time
import serial
import serial.tools.list_ports


def HiL_client_communication_serial_port(enable):


    if (enable):

        try:
            ports=serial.tools.list_ports.comports()
            for port, desc, hwid in sorted(ports):
                if desc == "STM32 Virtual Port":
                    print("COM PORT: {} used".format(port))
                    COM_PORT = port

            global HiL_serial_link
            HiL_serial_link = serial.Serial(COM_PORT, USB_BAUD_RATE, timeout=0.5)
            if HiL_serial_link.isOpen():
                print("serial port opened")
            
        except Exception as exc:
            raise Exception("Couldn't connect to server, check connection")

    else:
        
        try:
            HiL_serial_link.close()
            if not HiL_serial_link.isOpen():
                print("Serial port is closed")
        
        except Exception as exc:
            raise

# send messages
def HiL_client_communication_transmit(encoded_message):
    
    if VIRTUAL_SERVER: 
        pass
    
    else:
        try:
            HiL_serial_link.reset_input_buffer()
            HiL_serial_link.write(bytes(encoded_message))
            
        except Exception as exc:
            raise

# receive messages
def HiL_client_communication_receive():
    
    if VIRTUAL_SERVER: 
        return [2,1]

    else:
        try:
            recieved_message_array = list(HiL_serial_link.read(size=2))
            return recieved_message_array
            
        except Exception as exc:
            raise Exception("Client: Communication interrupted, check connection to server")

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

    try:
        value1 = recieved_message_array[0] #LSB
        value2 = recieved_message_array[1] #MSB

        return (value2 << 8) + value1
        
    except Exception as e:
        raise Exception("Client: Communication interrupted, check connection to server")
    


if __name__ == '__main__':
    pass
        


