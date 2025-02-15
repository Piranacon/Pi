# This example shows you a simple, non-interrupt way of reading Pico Inky Pack's buttons with a loop that checks to see if buttons are pressed.

import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pngdec import PNG

# Initialize the display
display = PicoGraphics(display=DISPLAY_INKY_PACK)

# you can change the update speed here!
# it goes from 0 (slowest) to 3 (fastest)
display.set_update_speed(0)

# a handy function we can call to clear the screen
def clear():
    display.set_pen(15)  # Set pen color to white (assuming 15 is white)
    display.clear()      # Clear the display
    display.update()     # Update the display to show changes

# Get the width and height of the display
WIDTH, HEIGHT = display.get_bounds()

# Clear the display initially
clear()
display.set_pen(0)  # Set pen color to black (assuming 0 is black)

# Draw rectangles on the display
display.rectangle(0, 0, int(WIDTH/4), int(HEIGHT /2))  # Top-left rectangle
display.rectangle(int(WIDTH/4)* 2 , 0, int(WIDTH/4), int(HEIGHT /2))  # Top-right rectangle

display.rectangle(int(WIDTH/4), int(HEIGHT /2),int((WIDTH/4)) , HEIGHT)  # Bottom-left rectangle
display.rectangle(int(WIDTH/4) *3, int(HEIGHT /2),int((WIDTH/4)) , HEIGHT)  # Bottom-right rectangle

# Update the display to show the rectangles
display.update()
