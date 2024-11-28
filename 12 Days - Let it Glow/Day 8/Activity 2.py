# Description: Turn on 4 LEDs on the ring
from machine import Pin
from neopixel import NeoPixel
import time

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

# Create a list of the LEDs to use
myleds = [0,3,6,9]

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)

for i in myleds:
    ring[i] = (0,0,10)
    ring.write()
