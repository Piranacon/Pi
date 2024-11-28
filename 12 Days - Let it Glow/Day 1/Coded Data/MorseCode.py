from machine import Pin
import time

led = Pin("LED", Pin.OUT)
short_press = 0.1
long_press = 0.3

# Define the Morse code dictionary
# So in this example this is not a machine friendly way to do this.
# It would be better to do this would be something like:
# morse_code = { 'A': [short_press, long_press], 'B': [long_press, short_press, short_press, short_press] }

morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..'
}

# Function to encode a string into Morse code
def encode_morse_code(text):
    encoded_text = ''
    for char in text:
        if char.upper() in morse_code:
            encoded_text += morse_code[char.upper()] + ' '
        else:
            encoded_text += char + ' '
    return encoded_text.strip()

# Encode the alphabet into Morse code
alphabet = 'hello world'
encoded_alphabet = encode_morse_code(alphabet)
for char in encoded_alphabet:
    if char == '.':
        led.on()
        time.sleep(short_press)
        led.off()
        time.sleep(short_press)
    elif char == '-':
        led.on()
        time.sleep(long_press)
        led.off()
        time.sleep(short_press)
    else:
        time.sleep(long_press)
