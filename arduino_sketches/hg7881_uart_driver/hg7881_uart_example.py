# requires python-serial
# apt-get install python-serial

import serial
import sys

KEY = chr(219) #0b11011011
#DEV = "/dev/ttyAMA0"
DEV = "/dev/ttyACM0"

#direction: 1 - forward; 0 - backward
def sendPayload(lDir, lSpeed, rDir, rSpeed):
    checkSum = (int(lDir) + int(lSpeed) + int(rDir) + int(rSpeed))%256
    payload = bytearray([   KEY,
                            chr(int(lDir)),     #left drive direction
                            chr(int(lSpeed)),   #left drive speed
                            chr(int(rDir)),     #right drive direction
                            chr(int(rSpeed)),   #right drive speed
                            chr(checkSum)
                        ])
    ser.write(payload)

ser = serial.Serial(DEV,9600)
# ser.open()
# opening causes an error for an unknown reason

sendPayload(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

#ser.close()
