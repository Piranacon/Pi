# Des
import time
from machine import Pin, ADC
from neopixel import NeoPixel
import Colours

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

# Define Bar graph display pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a variable for our reading
reading = 0

while True:
    
    reading = potentiometer.read_u16() # Read the potentiometer value and set this as our 'reading' variable value
    
    print(reading) # Print the reading value
    
    time.sleep(0.1) # short delay

    if reading <= 10000:
        seg1.value(0)
        seg2.value(0)   
        seg3.value(0)   
        seg4.value(0)
        seg5.value(0)
        
        GRBled1.fill((0,0,0))
        GRBled1.write()
        GRBled2.fill((0,0,0))
        GRBled2.write()
        
    elif 10000 < reading <= 20000: # If reading is less than or equal to 20000
         
        seg1.value(1)
        seg2.value(0)   
        seg3.value(0)   
        seg4.value(0)
        seg5.value(0)
    
        GRBled1.fill((Colours.colourList[0]))
        GRBled1.write()
        GRBled2.fill((Colours.colourList[len(Colours.colourList)-1]))
        GRBled2.write()
        
    elif 20000 < reading <= 30000: # If reading is less than or equal to 20000
         
        seg1.value(1)
        seg2.value(1)   
        seg3.value(0)   
        seg4.value(0)
        seg5.value(0)
    
        GRBled1.fill((Colours.colourList[1]))
        GRBled1.write()
        GRBled2.fill((Colours.colourList[len(Colours.colourList)-2]))
        GRBled2.write()
        
    elif 30000 < reading <= 40000: # If reading is between 20000 and 40000
    
        seg1.value(1)
        seg2.value(1)   
        seg3.value(1)   
        seg4.value(0)
        seg5.value(0)
     
        GRBled1.fill((Colours.colourList[2]))
        GRBled1.write()
        GRBled2.fill((Colours.colourList[len(Colours.colourList)-3]))
        GRBled2.write()
        
    elif 40000 < reading <= 50000: # If reading is greater than or equal to 40000
        seg1.value(1)
        seg2.value(1)   
        seg3.value(1)   
        seg4.value(1)
        seg5.value(0)
        
        GRBled1.fill((Colours.colourList[3]))
        GRBled1.write()
        GRBled2.fill((Colours.colourList[len(Colours.colourList)-4]))
        GRBled2.write()

    elif reading >= 50000: # If reading is greater than or equal to 40000
        seg1.value(1)
        seg2.value(1)   
        seg3.value(1)   
        seg4.value(1)
        seg5.value(1)
        
        GRBled1.fill((Colours.colourList[4]))
        GRBled1.write()
        GRBled2.fill((Colours.colourList[len(Colours.colourList)-5]))
        GRBled2.write()
