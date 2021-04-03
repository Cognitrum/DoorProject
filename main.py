# Python + Arduino-based Radar Plotter
#
# ** Works with any motor that outputs angular rotation
# ** and with any distance sensor (HC-SR04, VL53L0x,LIDAR)
#
from doorActivity import DoorActivity
import numpy as np
import serial,sys,glob,time
import serial.tools.list_ports as COMs
from datetime import datetime

def main():
    
    isOpen = False
    open = 45

    ser = serial.Serial('COM3',baudrate=9600) # match baud on Arduino
    ser.flush() # clear the port

    currentDoor = None

    while True:
        ser_bytes = ser.readline() # read Arduino serial data
        decoded_bytes = ser_bytes.decode('utf-8') # decode data to utf-8
        data = float ((decoded_bytes.replace('\r','')).replace('\n',''))
        if data <= open and isOpen == False:
            isOpen = True
            currentDoor = DoorActivity(time.time())
        elif data > open and isOpen == True:
            timeDuration = time.time() - currentDoor.startTime
            currentDoor.stopTime = time.time()
            currentDoor.duration = timeDuration
            print(data)
            print("Door activity results: \nTimeStart = {}\nTimeStop = {}\nTimeDuration = {}".format(datetime.fromtimestamp(round(currentDoor.startTime,2)), datetime.fromtimestamp(round(currentDoor.stopTime,2)), round(currentDoor.duration,2)))
            break
if __name__ == '__main__':
    main()