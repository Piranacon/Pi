# Description: This program will rotate through 3 colours on 4 LEDs
from machine import Pin
from neopixel import NeoPixel
import time

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)

# Create a list of the LEDs to use
myleds = [0,3,6,9]

# Create list to rotate through
rbg = [(0,0,10), (0,10,0),(10,0,0)]

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)

# Loop forever
while True:
    for t in range(3):
        # Loop through the LEDs 
        for i in myleds:
            # Loop through a range of 3
            # each placement can be incremented by 3 
            for j in range(3):
                # Set the LED colour
                ring[i+j] = rbg[(t+j) % 3]
            ring.write()
        time.sleep(1)
