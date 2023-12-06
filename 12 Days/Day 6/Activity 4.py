# Description: This program will light up a single LED and cycle through the red spectrum.
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

while True:
    
    for i in range(255):
        
        GRBled.fill((i,0,0))

        GRBled.write()
        
        time.sleep(0.005)
