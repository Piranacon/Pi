# Description: Loop forever and print a message when a button is pressed
from machine import Pin
import time

# Set up our button name and GPIO pin number
# Set the pin as an input and use a pull down
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True: # Loop forever

    time.sleep(0.2) # Short delay
    
    if redbutton.value() == 1: #If the red button is pressed
        print("Red button pressed")
        
    if greenbutton.value() == 1: #If the green button is pressed
        print("Green button pressed")
