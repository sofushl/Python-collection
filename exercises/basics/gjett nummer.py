from random import randint
play = "y"

while play == "y":
    num = randint(0, 1000)
    guess = int(input("Gjett et tall mellom 0 og 1000: "))
    while guess != num:
        if guess > num:
            print("Feil, gjettet ditt var for stort!")
        elif guess < num:
            print("Feil, gjettet ditt var for lite!")
        guess = int(input("Gjett et tall mellom 0 og 1000: "))
    print("Hurra du gjettet riktig!")
    play = str(input("Vil du spille igjen? y/n: "))
