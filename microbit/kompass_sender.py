from microbit import *
import radio

radio.on()
radio.config(channel=20)
display.show(Image.TARGET)

while True:
    c = compass.heading()
    if c > 315 or c <= 45:
        radio.send("N")
    elif c > 45 and c <= 135:
        radio.send("E")
    elif c > 135 and c <= 225:
        radio.send("S")
    elif c > 225 and c <= 315:
        radio.send("W")
