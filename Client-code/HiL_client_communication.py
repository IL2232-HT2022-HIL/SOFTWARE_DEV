
from HiL_config import CONTROLLER_REQUEST, CONTROLLER_OBJECTS, CONTROLLER_ACTIONS

def HiL_client_communication_encode(message):
    
    string_list = message.split(" ")
    
    controller_request = CONTROLLER_REQUEST[string_list[0]]
    controller_object  = CONTROLLER_OBJECTS[string_list[1]]

    if string_list[2] in CONTROLLER_ACTIONS:
        controller_action1 = CONTROLLER_ACTIONS[string_list[2]]
    else:
        controller_action1 = int(string_list[2])

    if len(string_list) != 4: # in case last byte not used
        controller_action2 = 0 # dummy byte
    
    elif string_list[3] in CONTROLLER_ACTIONS:
        controller_action2 = CONTROLLER_ACTIONS[string_list[3]]
    
    else:
        controller_action2 = int(string_list[3])
    
    return [controller_request, controller_object, controller_action1, controller_action2]


def HiL_client_communication_decode(message):
    pass

def HiL_client_communication_transmit(message):
    pass

def HiL_client_communication_receive(message):
    pass


# The following codes are just for debuging this file
if __name__=="__main__":
    pass