

class drink:
    def __init__(s, vol, pro, price):
        s.v = float(vol)
        s.p = float(pro)
        s.k = float(price)
        s.pp = ((s.p/100)*s.v)

    def ppp(s):
        s.pp = (s.p/100)*s.v
        return (s.pp)/s.k

while True:
    print(round(drink(input("Volume: "),input("Procent: "),input("Price: ")).ppp(),5))







