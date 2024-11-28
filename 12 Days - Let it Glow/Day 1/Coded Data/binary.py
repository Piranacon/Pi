from machine import Pin
import time

def pad_binary(bin_str):
    """
    Pads a binary string with leading zeros to make it 8 bits long.

    Args:
        bin_str (str): The binary string to pad.

    Returns:
        str: The padded binary string.
    """
    return '0' * (8 - len(bin_str)) + bin_str

led = Pin("LED", Pin.OUT)
short_press = 0.001
long_press = 0.002

text = "Go have fun and challenge"

binary = ' '.join(pad_binary(bin(ord(char))[2:]) for char in text)

print(binary)

# Loop through each character in the binary string
for char in binary:
    if char == ' ':
        # Turn off the LED for a long press
        led.off()
        time.sleep(long_press)
    else:
        # Set the LED value based on the binary digit
        led.value(int(char))
        time.sleep(short_press)

# Turn off the LED at the end
led.off()