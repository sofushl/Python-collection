def f(x):
    return 4*x**3 -4*x**2 -7*x -2

x = -1
while ( x < 10 ):
    if( -0.000001 < f(x) < 0.000001 ):
        print(x)
    x = x + 0.5
