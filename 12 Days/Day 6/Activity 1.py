# Description: This program will light up an LED with the color blue.
import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)
    
# Fill the LED with blue (GRB)
GRBled.fill((0,0,255))
        
# Write the data to the LED
GRBled.write()
