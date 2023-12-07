# Description: This program reads the value of the potentiometer and prints it to the console
from machine import ADC, Pin
import time

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

while True: # Loop forever

    print(potentiometer.read_u16()) # Read the potentiometer value

    time.sleep(0.3) # Short delay until the next reading
