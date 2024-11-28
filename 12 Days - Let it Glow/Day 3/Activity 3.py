# Description: This program will turn on and off an LED using a button.
from machine import Pin
import time

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
redled = Pin(14, Pin.OUT)

while True:

    time.sleep(0.2)
    
    if redbutton.value() == 1:
        print("Light OFF")
        redled.value(0) # LED pin LOW
        
    if greenbutton.value() == 1:
        print("Light ON")
        redled.value(1) # LED pin HIGH
