# Imports
import time
from machine import Pin
from neopixel import NeoPixel
import random

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)
r = 0
g = 0
b = 0
for _ in range(3):
    l = 0
    while l < 255:

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        # BEGIN: ed8c6549bwf9
        # Fill the LED with blue (GRB)
        GRBled.fill((g, r, b))
            
        # Write the data to the LED
        GRBled.write()
        # END: ed8c6549bwf9
        
        l += 1
        print(r, g, b)
        time.sleep(0.1) # 5 second delay
