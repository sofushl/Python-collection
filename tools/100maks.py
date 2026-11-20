
def statfind():
    inp = input("Write stats: 'h j s': ")
    inp = inp.split(" ")
    try:    
        return inp, (int(inp[0])+ int(inp[1]) + int(inp[2]))/3
    except:
        print("Error in input")
        return ["not", "horse"], 0

def listing():
    names = []
    stats = []
    while True:
        values, avg = statfind()
        name = values[0]+values[1]

        names.append(name)
        stats.append(avg)

        for i in range(len(names)):
            print(f"{names[i]} : {stats[i]}")    

listing()