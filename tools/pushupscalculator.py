g = float(input("Whats the goal: "))
s = float(input("Whats the finish time (in hours): "))
a = 0

while a < g:
    a = a + float(input("How many did you do: "))
    print ("Reps completed is " + str(a))
    
    b = float(input("Time (in hours): "))

    print ("You would need to do " + str(round(((g - a)/(s - b))+0.5, 1)) + "per hour to succeed")

print ("You are done!")
