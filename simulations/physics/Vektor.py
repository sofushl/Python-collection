from numpy import * 
del min, sum
from math import cos, acos, pi, sqrt

def v(x, y):
    return array([x,y])

def vec(name):
    return v(float(input(f"x of {name}: ")), float(input(f"y of {name}: ")))

def length(vector):
    return (vector[0]**2 + vector[1]**2)**(1/2)

def plusminus(mode):
    u = vec("u")
    v = vec("v")

    if mode == "+":
        return u+v
    if mode == "-":
        return u-v

def multiplicator(mode):
    vector = vec("vector")
    multiplicator = float(input("Multiplicator: "))

    result = multiplicator*vector

    if mode == "result":
        return result
    if mode == "print":
        print (f"{multiplicator} * {vector} = {result}")

def triangle():
    OA = vec("Point A")
    AC = vec("Vector AC")
    OB = vec("Point B")

    BA = OA - OB
    BC = BA + AC
    OC = OB + BC

    return OC

def parallelogram():
    OA = vec("A")
    OB = vec("B")
    OC = vec("C")

    OD1 = OA + OC - OB
    OD2 = OB + OA - OC
    OD3 = OC + OB - OA

    print(f"Unknown point = {OD1} V {OD2} V {OD3}")

def scalarproduct(mode):
    u = vec("u")
    v = vec("v")

    result = u[0]*v[0] + u[1]*v[1]

    if mode == "print":
        print (f"{u} * {v} = {result}")
    elif mode == "result":
        return result

def parallelvectors():
    u = vec("u")
    v = vec("v")

    if u[0]/v[0] == u[1]/v[1]:
        return v[0]/u[0]
    else:
        return False

def sidesofsquare():
    A = vec("point A")
    B = vec("point B")
    C = vec("point C")
    D = vec("point D")

    AB = B - A
    BC = C - B
    CD = D - C
    DA = A - D

    a = length(AB)
    b = length(BC)
    c = length(CD)
    d = length(DA)

    print("Lenghts of sides is: ", a, b, c, d)

    p = length(A-C)
    q = length(B-D)

    area = ( ( 4 * (q**2) * (p**2) - (a**2 - b**2 + c**2 - d**2)**2 )**(1/2) ) /4

    print(f"Area of square = {round(area, 6)}")

def angle(u, v):
    print ((u[0]*v[0] + u[1]*v[1]) / (length(u)*length(v)))
    return acos( (u[0]*v[0] + u[1]*v[1]) / (length(u)*length(v)) ) * ( 180.0 / pi )

def cmd(value):
    return inp.lower() == value

def main():
    global inp
    while True:
        try:
            inp = input("Vector calculator type: ")

            if cmd("l") or cmd("length") or cmd("pythagoras") or cmd("0"):
                print("Initializing length calculator")
                print(f"The length of the vector is {length(vec('vector'))}")

            elif cmd("+") or cmd("p") or cmd("plusminus") or cmd("1"):
                print("Initializing plus calculator")
                print("u + v = ", plusminus("+"))

            elif cmd("-") or cmd("m") or cmd("plusminus") or cmd("-1"):
                print("Initializing minus calculator")
                print("u - v = ", plusminus("-"))

            elif cmd("*") or cmd("times") or cmd("const") or cmd("multiplicator") or cmd("2"):
                print("Initializing multiplicator")
                multiplicator("print")

            elif cmd("point") or cmd("triangle") or cmd("findpoint") or cmd("3"):
                print("Initializing unknown in triangle calculator")
                print("Unknown point = ", triangle())

            elif cmd("parallelogram") or cmd("findunknown") or cmd("4"):
                print("Initializing unknown in parallelogram calculator")
                parallelogram()

            elif cmd("multiplicate") or cmd("scalarproduct") or cmd("scalar") or cmd("5"):
                print("Initializing scalarproduct calculator")
                scalarproduct("print")

            elif cmd("parallel") or cmd("parallelvectors") or cmd("line") or cmd("6"):
                print("Initializing parallelvectors calculator")
                p = parallelvectors()
                if p:
                    print("The vectors are parallel and propotionalityconstant is", p)
                else:
                    print("The vectors are not parallel")

            elif cmd("sidesofsquare") or cmd("sides") or cmd("square") or cmd("area") or cmd("s") or cmd("7"):
                print("Initializing squaresides calculator")
                sidesofsquare()

            elif cmd("corner") or cmd("angle") or cmd("8"):
                print(f"The corner angle is: {angle(vec('u'),vec('v'))}")

            else:
                print(inp, "is not a valid command")

        except:
            print("An exception occurred")

