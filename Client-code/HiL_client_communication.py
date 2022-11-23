
from HiL_config import CONTROLLER_REQUEST, CONTROLLER_OBJECTS, CONTROLLER_ACTIONS

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


def HiL_client_communication_transmit(encoded_message): # TO BE IMPLEMENTED
    pass


def HiL_client_communication_receive(): # TO BE IMPLEMENTED
    return [0,0]




