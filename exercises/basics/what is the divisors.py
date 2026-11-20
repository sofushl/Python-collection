while True:
    inp = int(input("type a number:"))
    alist = range(2, inp//2+1)
    nlist = []
    
    for a in alist:
        if (int(inp) % a) == 0:
            nlist.append (a) 

    print(inp, "can be divided by", nlist)

