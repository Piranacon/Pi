# This program measures the distance from an object using an ultrasonic sensor.

from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)


def ultra():
    """
    Measures the distance from an object using an ultrasonic sensor.
    
    Returns:
        distance (float): The distance from the object in centimeters.
    """
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    return distance

while True:
    distance = ultra()
    print("The distance from object is: {} cm ".format(distance))
    utime.sleep(2)