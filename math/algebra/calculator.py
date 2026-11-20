from math import sqrt

a = float(input("tall 1: "))
b = float(input("tall 2: "))
u = str(input("operasjon (+, -, *, /, ^, sqrt): "))

if u == ("+"):
    s = a + b
elif u == ("-"):
    s = a - b
elif u == ("*"):
    s = a * b
elif u == ("/"):
    s = a / b
elif u == ("^"):
    s = a**b
elif u == ("sqrt"):
    s = sqrt(a)
else:
    s = str("du må skrive +, -, *, /, ^ eller sqrt")

print (s)
