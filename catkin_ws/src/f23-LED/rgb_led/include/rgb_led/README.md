To work with pigppio, you need to run the pigpio daemon with the "sudo pigpiod" command.

In order to set a color on the LED, it is necessary to call the setRGB(...) function, passing into it the LED number and an array of the form [1,1,1] containing information about the presence or absence of any color component ([r, g , b]).

Setting the color of the LED occurs in two steps: changing the bits that will be fed to the pins of the shift register (the BITS variable) and directly updating the bit values on the shift register.

The setLEDBrightness(...) function updates the value of any component of the LED using the component offset and the LED number.

The function setComponent(...) directly deletes the bit (delBit) which needs to be changed and sets a new value (newBit).

The inverseBits(...) function inverts the bit values for the case of LEDs with a common anode.

The setBits(...) function sets values on the pins, outBits(...) latches the value.

Pins:

SDI - Data
RCLK - Time sequence input of shift register
SRCLK - Time sequence input of storage register. 
