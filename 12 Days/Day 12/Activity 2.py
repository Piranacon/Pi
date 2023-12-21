# Description: This program shows how to use the LCD
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import time

# Define LCD I2C pins/BUS/address
SDA = 14
SCL = 15
I2C_BUS = 1
LCD_ADDR = 0x27

# Define LCD rows/columns
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16

lcdi2c = I2C(I2C_BUS, sda=machine.Pin(SDA), scl=machine.Pin(SCL), freq=400000)
lcd = I2cLcd(lcdi2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

# Our variables
mystring = "String variable" # String
myinteger = 44         # Integer
myfloat = 9.445589     # Float

# Just a function to sleep and then clear the LCD
# Saves lines after each example!
def clearLCD():

    time.sleep(3)
    lcd.clear()

##### Example Program Start #####

# This is how you show basic text
lcd.putstr("Sometimes you")
time.sleep(3)

# This is how you clear the display
# Do this before you send new data to be displayed
# This is how you move the cursor
# We moved it to the second row
# 1st number is column (X), 2nd number is row (Y)
# Numbers start at zero
# (0,0) is the 1st column, 1st row
lcd.move_to(0, 1)
lcd.putstr("Need to play the")
clearLCD()

# This is how you show a variable
# Variables can be strings, integers or floats
# 'str' converts them to a string
# Here are three examples:
lcd.putstr(str("fool")) # String
clearLCD()

