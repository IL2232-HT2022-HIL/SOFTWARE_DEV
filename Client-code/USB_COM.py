#coding=utf-8
import time
import serial
IsOpen=True;
InputStr=""
# open serial port
def open_ser():
    port = 'com3'
    baudrate = 115200
    try:
        global ser
        ser = serial.Serial(port, baudrate, timeout=0.5)
        if (ser.isOpen() == True):
            print("serial port opened")
    except Exception as exc:
        print("Serial port open exception", exc)

# send massages
def send_msg():
    try:
        print("please input")
        send_datas = input()
        InputStr=send_datas.encode("utf-8")
        ser.write(send_datas.encode("utf-8"))
        print("send message:", send_datas)
    except Exception as exc:
        print("error", exc)

# receive messages
def read_msg():
    try:
        print("waiting for receive message")
        time.sleep(1)
        #while True:
        data = ser.read(ser.in_waiting).decode('gbk')
        if data != '':
             for char_index in range(len(data)):
               #if str(data[char_index] )in InputStr :
               if data[char_index]!="\x00":
                print("message received:", data[char_index])
        if data=='break':
            IsOpen=False
            print("serial port closed")
            close_ser()
    except Exception as exc:
        print("receive error", exc)

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

if __name__ == '__main__':
    open_ser()  # open serial port
    while IsOpen:
     send_msg()  # send message
     read_msg()  # receive message
     #close_ser()  # close serial port