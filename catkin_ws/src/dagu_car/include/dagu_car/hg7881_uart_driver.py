#!/usr/bin/python

# Wrapping UART communication with connected to Arduino HG7881 driver
#
# date:    02 may 2017
#
# authors: Constantin Chayka <pro100kot14@gmail.com>
#          Olesya Tishencko <lesya.tishencko2012@yandex.ru>
#          Anatoly Bendrikovsky <bendrikovski@gmail.com>

from math import fabs, floor
import serial

class HG7881ArduinoDriver:
    LEFT_MOTOR_MIN_PWM = 60  # Minimum speed for left motor
    LEFT_MOTOR_MAX_PWM = 255  # Maximum speed for left motor
    RIGHT_MOTOR_MIN_PWM = 60  # Minimum speed for right motor
    RIGHT_MOTOR_MAX_PWM = 255  # Maximum speed for right motor
    SPEED_TOLERANCE = 1.e-2  # speed tolerance level


    def __init__(self, verbose=False, debug=False, left_flip=False, right_flip=False):
        self.verbose = verbose or debug
        self.debug = debug

        # direction: 1 - forward; 0 - backward
        DEV = "/dev/ttyAMA0"
        #DEV = "/dev/ttyACM0"

        self.ser = serial.Serial(DEV, 9600)
        self.KEY = chr(219)  # 0b11011011

        self.left_sgn = 1.0
        if left_flip:
            self.left_sgn = -1.0

        self.right_sgn = 1.0
        if right_flip:
            self.right_sgn = -1.0

        self.leftSpeed = 0.0
        self.rightSpeed = 0.0
        self.updatePWM()

    def sendPayload(self,lDir, lSpeed, rDir, rSpeed):
        checkSum = (int(lDir) + int(lSpeed) + int(rDir) + int(rSpeed)) % 256
        payload = bytearray([self.KEY,
                             chr(int(lDir)),  # left drive direction
                             chr(int(lSpeed)),  # left drive speed
                             chr(int(rDir)),  # right drive direction
                             chr(int(rSpeed)),  # right drive speed
                             chr(checkSum)
                             ])
        self.ser.write(payload)

    def PWMvalue(self, v, minPWM, maxPWM):
        pwm = 0
        if fabs(v) > self.SPEED_TOLERANCE:
            pwm = int(floor(fabs(v) * (maxPWM - minPWM) + minPWM))
        return min(pwm, maxPWM)

    def updatePWM(self):
        vl = self.leftSpeed * self.left_sgn
        vr = self.rightSpeed * self.right_sgn

        if fabs(vl) < self.SPEED_TOLERANCE:
            pwml = 0
        else:
            pwml = self.PWMvalue(vl, self.LEFT_MOTOR_MIN_PWM, self.LEFT_MOTOR_MAX_PWM)

        if fabs(vr) < self.SPEED_TOLERANCE:
            pwmr = 0
        else:
            pwmr = self.PWMvalue(vr, self.RIGHT_MOTOR_MIN_PWM, self.RIGHT_MOTOR_MAX_PWM)

        if self.debug:
            print "vl = %5.3f, vr = %5.3f, pwml = %3d, pwmr = %3d" % (vl, vr, pwml, pwmr)

        self.sendPayload(0 if vl < 0 else 1, pwml, 0 if vr < 0 else 1, pwmr)

    def setWheelsSpeed(self, left, right):
        self.leftSpeed = left
        self.rightSpeed = right
        self.updatePWM()

    def __del__(self):
        self.setWheelsSpeed(0,0)


# Simple example to test motors
if __name__ == '__main__':
    from time import sleep

    N = 255
    delay = 100. / 1000.

    dagu = HG7881ArduinoDriver()

    # accelerate forward
    for i in range(N):
        dagu.setWheelsSpeed((1.0 + i) / N, (1.0 + i) / N)
        sleep(delay)
    # decelerate forward
    for i in range(N):
        dagu.setWheelsSpeed((-1.0 - i + N) / N, (-1.0 - i + N) / N)
        sleep(delay)
    del dagu
