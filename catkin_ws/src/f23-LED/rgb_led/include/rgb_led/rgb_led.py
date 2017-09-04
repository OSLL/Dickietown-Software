#!/usr/bin/env python
# ================================================
#
#   Extend use of 16 LEDs with pair of 74HC595.
#   Pair of 74HC595 takes 16 bits.
#   Low 15 bits affect the LEDs.
#   16 bits convert to int
#   Components of the RGB LED have order rgb
#   LEDs are numbered from right to left
#   0_000_000_000_000_000
#   0_rgb_rgb_rgb_rgb_rgb
#
# =================================================

import time
import pigpio

class RGB_LED():
    # ===============   LED Mode Define ================
    LED_COMMON_ANODE = True
    SDI = 17 #11  # 14(74HC) data
    RCLK = 18 #12  # 12(74HC) ST_CP latch
    SRCLK = 27 #13  # 11(74HC) SH_CP shift
    LEDS_COUNT = 5
    # =================================================

    OFFSET_RED = 0
    OFFSET_GREEN = 1
    OFFSET_BLUE = 2
    off = [0, 0, 0]

    def __init__(self, debug=False):
        #self.BITS = format(0, '016b')  # 0_000_000_000_000_000
        self.BITS = 0
        self.setup()


    def setup(self):
        self.pi = pigpio.pi()
        self.pi.set_mode(self.SDI, pigpio.OUTPUT)
        self.pi.set_mode(self.RCLK, pigpio.OUTPUT)
        self.pi.set_mode(self.SRCLK, pigpio.OUTPUT)
        self.pi.write(self.SDI, 0)
        self.pi.write(self.RCLK, 0)
        self.pi.write(self.SRCLK, 0)

    def setRGB(self, led, color):
        self.setLEDBrightness(led, self.OFFSET_RED, color[0])
        self.setLEDBrightness(led, self.OFFSET_GREEN, color[1])
        self.setLEDBrightness(led, self.OFFSET_BLUE, color[2])
        self.update()

    # def setRGBint24(self, led, color):
    #     r = color >> 16 & 0xFF
    #     g = color >> 8 & 0xFF
    #     b = color >> 0 & 0xFF
    #     self.setRGBvint8(led, [r, g, b])
    #
    # def setRGBvint8(self, led, color):
    #     self.setLEDBrightness(led, self.OFFSET_RED, color[0])
    #     self.setLEDBrightness(led, self.OFFSET_GREEN, color[1])
    #     self.setLEDBrightness(led, self.OFFSET_BLUE, color[2])

    def setLEDBrightness(self, led, offset, brightness):
        self.setComponent(3 * led + offset, brightness)

    def setComponent(self, bit, brightness):
        self.delBit(bit)
        self.newBit(bit, brightness)

    #   =================================================
    #    Part of GPIO output by means 74HC595
    #   =================================================

    def delBit(self, bit):
        del_led = 2 ** bit
        del_led = int(~del_led & 0xffff)
	self.BITS = int(self.BITS) & del_led

    def newBit(self, bit, brightness):
	if brightness == 0:
	    newLed = 0
	else:
	    newLed = 2 ** bit
    #    newLed = brightness * 2 ** bit
	self.BITS = int(self.BITS + newLed)

    def inverseBits(self):
	return int(~int(self.BITS) & 0xffff)

    def setBits(self, BITS):
        if self.LED_COMMON_ANODE:
	    dat = self.inverseBits()
        else:
            dat = self.BITS

        for bit in range(0, 16):
            if 0x8000 & (dat << bit) == 0:
                self.pi.write(self.SDI, 0)
            else:
                #After multiplying on 0x8000 we know the highest bit of a number
                self.pi.write(self.SDI, 1)
            self.pi.write(self.SRCLK, 1)
            time.sleep(0.001)
            self.pi.write(self.SRCLK, 0)

    def outBits(self):
        self.pi.write(self.RCLK, 1)
        time.sleep(0.001)
        self.pi.write(self.RCLK, 0)

    def update(self):
        self.setBits(self.BITS)
        self.outBits()

    def __del__(self):
	self.pi.stop()

