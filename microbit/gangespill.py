from microbit import *
from random import randint

while True:
    a = randint(1, 9)
    b = randint(1, 9)
    display.scroll(str(a) + "x" + str(b))
    sleep(200)
    display.scroll("Digit 1:")
    sleep(200)
    aa = 0
    while True:
        display.scroll(str(aa))
        if button_a.is_pressed():
            aa += 1
        if button_b.is_pressed():
            break
    display.scroll("Digit 2:")
    sleep(200)
    ba = 0
    while True:
        display.scroll(str(ba))
        if button_b.is_pressed():
            ba += 1
        if button_a.is_pressed():
            break
    answer = [str(aa), str(ba)]
    answer = int("".join(answer))
    if answer == a * b:
        display.scroll("Correct! {}{} == {}".format(aa, ba, a*b))
    else:
        display.scroll("Wrong! {}{} != {}".format(aa, ba, a*b))
