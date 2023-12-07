# Description: This program will read the value of a potentiometer and display a different colour on an LED depending on the value of the potentiometer.
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)
# Define a few basic GRB colour variables
red = 0,255,0
amber = 255,175,150
green = 255,0,0

# Create a variable for our reading
reading = 0

while True:
    
    reading = potentiometer.read_u16() # Read the potentiometer value and set this as our 'reading' variable value
    
    print(reading) # Print the reading value
    
    time.sleep(0.1) # short delay
    
    if reading <= 20000: # If reading is less than or equal to 20000
         
        GRBled1.fill((red))
        GRBled1.write()
        GRBled2.fill((green))
        GRBled2.write()
        
    elif 20000 < reading < 40000: # If reading is between 20000 and 40000
    
        GRBled1.fill((amber))
        GRBled1.write()
        GRBled2.fill((amber))
        GRBled2.write()
        
    elif reading >= 40000: # If reading is greater than or equal to 40000
            
        GRBled1.fill((green))
        GRBled1.write()
        GRBled2.fill((red))
        GRBled2.write()
