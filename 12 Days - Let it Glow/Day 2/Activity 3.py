# Description: Toggles the light on and off every second
from machine import Pin
import time

red = Pin(14, Pin.OUT)

red.value(1)
time.sleep(1)

red.value(0)
time.sleep(1)

red.value(1)
time.sleep(1)

red.value(0)
time.sleep(1)
