import random
c = 0
w = 0
while True:
    ca = random.randint(1, 9)
    

    a = input("guess a number betwwen 1 and 9(write stop now to end the game):")
    if a == "stop":
        break
    while True:
        if int(a) == int(ca):
            print (a, "is the correct answer")
            c = c + 1
            break
        elif int(a) < int(ca):
            print ("your answer is too low")
            w = w + 1
        elif int(a) > int(ca):
            print ("your answer is too high")
            w = w + 1
        a = input("guess a number betwwen 1 and 9:")

print ("you made", c, "correct answers, and", w, "wrong answers")
