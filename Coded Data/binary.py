from machine import Pin
import time

def pad_binary(bin_str):
    return '0' * (8 - len(bin_str)) + bin_str

led = Pin("LED", Pin.OUT)
short_press = 0.001
long_press = 0.002

text = "Go have fun and challenge"
binary = ' '.join(pad_binary(bin(ord(char))[2:]) for char in text)
print(binary)
for char in binary:
    if char == ' ':
        led.off()
        time.sleep(long_press)
    else:
        led.value(int(char))
        time.sleep(short_press)
        
led.off()