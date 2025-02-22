import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_INKY_PACK
from pngdec import PNG

display = PicoGraphics(display=DISPLAY_INKY_PACK)

display.set_update_speed(2)


def clear():
    display.set_pen(15)
    display.clear()
    display.update()

clear()
display.set_pen(0)
WIDTH, HEIGHT = display.get_bounds()

display.set_font("bitmap14_outline")
#display.set_thickness(2)
display.text("", 0, 20, scale=2)

display.set_font("bitmap14_outline")
display.text("", 0, 45, scale=1)

display.set_font("bitmap8")
display.text("", 0, 60, scale=1, wordwrap=int((WIDTH / 4) * 3))

display.set_font("bitmap6")
display.text("Tel:", 0, 75, scale=1, wordwrap=int((WIDTH / 4) * 3))
display.text("Email: ", 0, 85, scale=1, wordwrap=int((WIDTH / 4) * 3))


png = PNG(display)
png.open_file("")
png.decode(int(WIDTH/4) *3, 20, mode=5)  
display.update()
