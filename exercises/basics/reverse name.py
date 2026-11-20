name = list(input("Type your name: "))

def reverse(name):
    eman = []
    for i in range(1, len(name)+1):
        eman.append(name[-i])
        

    return ''.join(eman)

print(str(reverse(name)))
