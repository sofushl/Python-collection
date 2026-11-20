from microbit import *
import radio

radio.on()
radio.config(channel=20) #Skrur på og instiller radio
display.show(Image.SAD)


while True: #Løkke som stopper og lar koden fortsette når den mottar "start" eller knap A trykkes
    message = radio.receive()
    if message == "start" or button_a.is_pressed():
        break

t = 0

with open("mufile.txt","w") as f:

    display.show(Image.HAPPY)

    while True:

        temp = temperature()
        f.write(str(temp)+ "\n") #Skriver ned temperatur og lager linjeskift

        light = pin0.read_analog()
        f.write(str(light)+ "\n") #Skriver ned lysnivå og lager linjeskift

        sleep(600000) #600000 = 10min
        t += 1

        message = radio.receive()
        if message == "stop" or button_b.was_pressed(): #stopper koden når den mottar "stop" eller knap B trykkes
            radio.send("stopped")
            break

display.show(Image.SAD)
