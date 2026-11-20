from microbit import *

while True:
    if button_a.is_pressed():
        display.show(Image.ARROW)
    elif button_b.is_pressed():
        display.show(Image.ARROW_W)
    else:
        display.show(Image.TARGET)

display.clear()
