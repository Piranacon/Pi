# Description: This program will toggle the red LED when the red button is pressed.
from machine import Pin
import time

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
redled = Pin(14, Pin.OUT)

while True:

    time.sleep(0.2)
    
    if redbutton.value() == 1:
        redled.toggle()
