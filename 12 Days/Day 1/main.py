from machine import Pin

led = Pin(25, Pin.OUT)

#  Theres a couple of ways of handling the on/off state of the LED 

# On
# led.on()
# led.value(1) # Turn on the LED

# Off
# led.off()
# led.value(0) # Turn off the LED

# Toggle
led.toggle() # This sets the value to the opiste it currently is 
# led.value(led.value() ==0) # We check if the current value is set to 0, if so then we are setting the value to 1 (ie true)