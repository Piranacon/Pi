# Description: Blink an LED on and off 10 times
from machine import Pin
import time

## Pin setup ##
red = Pin(14, Pin.OUT) # Set GPIO 14 as an output

## Program Start ##
for i in range(10): # Run the indented code below 10 times
    
    red.value(1) # LED on
    time.sleep(0.5) # Wait half a second

    red.value(0) # LED off
    time.sleep(0.5) # Wait half a second
    
print("Program finished")
