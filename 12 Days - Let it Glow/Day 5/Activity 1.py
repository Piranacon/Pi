# Description: Read the state of 5 switches and print the state of each switch to the console
from machine import Pin
import time

# Set up switch input pins
dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if dip1.value() == 1:
        print("Switch 1: ON")
            
    if dip2.value() == 1:
        print("Switch 2: ON")
        
    if dip3.value() == 1:
        print("Switch 3: ON")
        
    if dip4.value() == 1:
        print("Switch 4: ON")
        
    if dip5.value() == 1:
        print("Switch 5: ON")
        
    print("-------------") # Print a divider
        
    time.sleep(5) # 5 second delay

