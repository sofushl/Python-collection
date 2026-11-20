s1 = float(input("Gi meg trekant sidelengde 1"))
s2 = float(input("Gi meg trekant sidelengde 2"))
s3 = float(input("Gi meg trekant sidelengde 3"))

def check(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

if s1 > s2 and s1 > s3:
    if check(s2, s3, s1):
        print(f"{s1}, {s2} og {s3} er en pytagoreisk trippel")
    else:
        print (f"{s1}, {s2} og {s3} er ikke en pytagoreisk trippel")
    
elif s2 > s1 and s2 > s3:
    if check(s1, s3, s2):
        print (f"{s1}, {s2} og {s3} er en pytagoreisk")
    else:
        print (f"{s1}, {s2} og {s3} er ikke en pytagoreisk trippel")
        
elif s3 > s1 and s3 > s2:
    if check(s1, s2, s3):
        print (f"{s1}, {s2} og {s3} er en pytagoreisk trippel")
    else:
        print (f"{s1}, {s2} og {s3} er ikke en pytagoreisk trippel")

else:
    print (f"{s1}, {s2} og {s3} er ikke en pytagoreisk trippel")
