word = str(input("Løsningsord: "))

for i in range(3):
    for i in range(90000):
        if i < 30000:
            print("skjuler.")
        elif i < 60000:
            print("skjuler..")
        else:
            print("skjuler...")

states = ['''

             
      
      
      
      
=========''','''
      +
      |
      |
      |
      |
      |
=========''','''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  X   |
 /|\  |
 / \  |
      |
=========''']

letters = list([*word])

remainingletters = list(letters[0:len(letters)])

guessedletters = []
for i in range(len(remainingletters)):
    guessedletters.append("0")

guesses = []
s = 0

while True:
    
    print(states[s])
    print("".join(guessedletters))
    
    if len(remainingletters)==0:
        print("Du gettede det!")
        break
    elif s == 10:
        print("Du døde!")
        break 

    guess = str(input("\nGet en bokstav: "))
    print("\r")

    if guess in guesses:
        print("Det har du allerede gettet!")
    elif guess in remainingletters:
        print("Woah det er rigtig!!!")
        for i in range(len(letters)):
            if guess == letters[i]:
                guessedletters[i] = letters[i]
                remainingletters.remove(guess)  
                

    else:
        print("NEI, det er FORKERT!")
        s +=1
    
    guesses.append(guess)
