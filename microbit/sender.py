from microbit import *
import radio

radio.on()
radio.config(channel=20) #Skrur på og instiller radio
display.show(Image.SAD)

while True: #Løkke som stopper, lar koden fortsette og sender "start" til den andre microbiten når knap A trykkes
    if button_a.is_pressed():
        radio.send("start")
        display.show(Image.HAPPY)
        break

i = 0
message = radio.receive

while True:
    if button_b.is_pressed():  #Sender "stop" til den andre microbiten når knap B trykkes
        radio.send("stop")
        break
    else:
        display.show(Image.HAPPY)

display.show(Image.SAD)
