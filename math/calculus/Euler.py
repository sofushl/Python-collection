t = 1.0

while t > 0.00000000001:
    e = (1+2*t)**(1/t)
    print(f"t = {t} gir e = {round(e, 10)}")
    t=t/10
