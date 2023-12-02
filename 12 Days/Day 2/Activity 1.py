# Description: Code does exactly what day 1 activity 1 does. 
# But this time, it uses a different pin for the LED.
from machine import Pin

# Note: We're calling the GPIO pins by their GPIO number, not their physical pin number.
blockLED = Pin(14, Pin.OUT)

blockLED.value(1)
print("Block LED on!")
