p1 = 0
while p1 != "rock" and p1 != "paper" and p1 != "scissors":
    p1 = input("Player 1: rock, paper or sciccors?")
    if p1 != "rock" and p1 != "paper" and p1 != "scissors":
        print ("invalid answer")

p2 = 0
while p2 != "rock" and p2 != "paper" and p2 != "scissors":
    p2 = input("Player 2: rock, paper or sciccors?")
    if p2 != "rock" and p2 != "paper" and p2 != "scissors":
        print ("invalid answer")

if p1 == ("rock") and p2 == ("paper"):
    print ("player 2 wins")
if p1 == ("sciccors") and p2 == ("rock"):
    print ("player 2 wins")
if p1 == ("paper") and p2 == ("sciccors"):
    print ("player 2 wins")

if p2 == ("rock") and p1 == ("paper"):
    print ("player 1 wins")
if p2 == ("sciccors") and p1 == ("rock"):
    print ("player 1 wins")
if p2 == ("paper") and p1 == ("sciccors"):
    print ("player 1 wins")

if p2 == p2:
    print ("it's a tie")
