# This is a demo program for the Pico WH Starter Kit
# It will flash the LED on and off every 0.5 seconds

from machine import Pin
import time

led = Pin("LED", Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)