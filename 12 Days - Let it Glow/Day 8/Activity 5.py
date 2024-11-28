# Description: This program will light up the LEDs in a ring one at a time, then turn them off one at a time.
from machine import Pin
from neopixel import NeoPixel
import time

# Define the strip pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)
# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)

# Description: This program will light up the LEDs in a ring one at a time, then turn them off one at a time.
def clockwise():
    for i in range(12):
        
        ring[i] = (5,0,5)
        ring.write()
        
        # Show the light for this long
        time.sleep(0.09)
        
        #Clear the ring at the end of each loop
        ring.fill((0,0,0))
        ring.write()

# Description: This program will light up the LEDs in a ring one at a time, then turn them off one at a time.
def anticlockwise():
    for i in reversed (range(12)):
        
        ring[i] = (5,0,5)
        ring.write()
        
        # Show the light for this long
        time.sleep(0.09)
        
        #Clear the ring at the end of each loop
        ring.fill((0,0,0))
        ring.write()

while True:
    clockwise()
    anticlockwise()