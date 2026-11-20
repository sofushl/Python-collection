def f(x):
    if x < 1:
        return -2*x**2 + 4
    else:
        return x**2 -4*x + 3
    return 

a = float(input("velg en verdi for a: "))

t = 0.1
while t > 0.0000001:
    print(f"f({str(round(a-t, 7))}) = {round(f(a-t), 50)}")
    t /= 10

t = 0.1
while t > 0.0000001:
    print(f"f({str(round(a+t, 7))}) = {round(f(a+t), 50)}")
    t /= 10
