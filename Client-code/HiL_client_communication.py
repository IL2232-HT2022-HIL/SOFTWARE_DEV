
from HiL_config import CONTROLLER_REQUEST, CONTROLLER_OBJECTS, CONTROLLER_ACTIONS

import time
import serial
IsOpen=True;

# open serial port
def open_ser():
    port = 'COM6'
    baudrate = 115200
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=0.5)
        if (ser.isOpen() == True):
            print("serial port opened")
    
    except Exception as exc:
        print("Serial port open exception", exc)


# close serial port
def close_ser():
    try:
        ser.close()
        if ser.isOpen():
            print("")
        else:
            print("Serial port is closed")
    except Exception as exc:
        print("Serial port closing exception", exc)


# send messages
def HiL_client_communication_transmit(encoded_message):
    
    try:
        ser.write(bytes(encoded_message))
        
    except Exception as exc:
        print("error", exc)

# receive messages
def HiL_client_communication_receive():
    try:
        data = list(ser.read(ser.in_waiting))
        return data[0:4:]
        
    except Exception as exc:
        print("receive error", exc)



def HiL_client_communication_encode(message):
    
    string_list = message.split(" ")
    
    controller_request = CONTROLLER_REQUEST[string_list[0]]
    controller_object  = CONTROLLER_OBJECTS[string_list[1]].object_value

    if string_list[2] in CONTROLLER_ACTIONS:
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
    open_ser()  # open serial port
    while IsOpen:
        HiL_client_communication_transmit([65,65,65,65])  # send message
        time.sleep(0.1)
        print(HiL_client_communication_receive())  # receive message
        time.sleep(2)
        













