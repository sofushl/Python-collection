u18 = 0
o18 = 0
o67 = 0

L = [21, 23, 85, 6, 17, 45, 90, 32, 62, 13, 70, 65, 40, 68]

def check(age):
    if age < 18:
        return "u18"
    elif age >= 18 and age < 67:
        return "o18"
    elif age >= 67:
        return "o67"

print (len(L))
for age in L:
    result = check(age)
    if result == "u18":
        u18 += 1
    elif result == "o18":
        o18 += 1
    elif result == "o67":
        o67 += 1
    else:
        print(age)
        
print (f"Det er {u18} under 18, {o18} 18 eller eldre og {o67} 67 eller eldre")
