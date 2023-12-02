# Description: Blinks an LED on and off
from machine import Pin
import time

# Pin setup
red = Pin(14, Pin.OUT) # Set GPIO 14 as an output

## Program Start ##
while True: # Loop forever

    red.value(1) # LED on
    time.sleep(0.5) # Wait half a second

    red.value(0) # LED off
    time.sleep(0.5) # Wait half a second
