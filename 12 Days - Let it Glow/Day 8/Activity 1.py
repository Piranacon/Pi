# Description: This program will light up the first LED on the ring in red
from machine import Pin
from neopixel import NeoPixel

# Define the ring pin number (2) and number of LEDs (12)
ring = NeoPixel(Pin(2), 12)
        
# Select the first LED (0)
# Set the RGB colour (red)
ring[0] = (255,0,0)

# Send the data to the ring
ring.write()