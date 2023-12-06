# Description: This program will make the LED fade from green to red and back again.
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

while True:
    
    for i in range(255): # Changes i by +1 each loop, from 0 to 255
        
        GRBled.fill((i,0,0)) # Uses the i value as the G in GRB

        GRBled.write()
        
        time.sleep(0.005) # Very short delay
        
    for i in reversed (range(255)): # Changes i by -1 each loop, from 255 to 0
        
        GRBled.fill((0,i,0)) # Uses the i value as the R in GRB

        GRBled.write()
        
        time.sleep(0.005) # Very short delay
