from math import sqrt

a = float(input('what is a? '))
b = float(input('what is b? '))
c = float(input('what is c? '))

if b**2-4*a*c > 0:
    x1 = (-b+sqrt(b**2-4*a*c))/2*a
    x2 = (-b-sqrt(b**2-4*a*c))/2*a
    print(f"Nullpunktene er {x1} og {x2}")
elif b**2-4*a*c == 0:
    x = -b/2*a
    print(f"Nullpunket er {x}")
else:
    print("Din funkjson har ingen nullpunkter")
    
