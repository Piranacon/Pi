# Description: This program will increment and decrement a counter variable based on button presses.
from machine import Pin
import time

# Set up input pins
redbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up counter variable
count = 0 # Start at zero

while True:

    time.sleep(0.2)
    
    if redbutton.value() == 1:
        count = count -1 #Reduce count by 1
        print(count) #Print our updated count
        
    if greenbutton.value() == 1:
        count = count +1 #Increase count by 1
        print(count) #Print our updated count
