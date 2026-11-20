while True:
    alist = [1, 1, 2, 3, 5, 8, 13, 4, 34, -55, 0]
    inp = int(input("type a number:"))

    for a in alist:
        if a < inp: print(a)
