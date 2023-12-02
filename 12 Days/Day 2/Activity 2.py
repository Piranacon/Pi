# Description: Turns both lights on
from machine import Pin

green = Pin(25, Pin.OUT)
red = Pin(14, Pin.OUT)

green.value(1)
red.value(1)

print("Both LEDs ON!")

# I love the fact that, samples bring up an unexpected result!
# If you don't them off and continue to run the other samples the
# onboard LED will stay on for all of the samples.
print("Don't forget to turn them off!")
# green.value(0)
# red.value(0)