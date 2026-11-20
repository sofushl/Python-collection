a = str(input("Write something: "))

a = a.split()

b = []

for i in a:
    b.insert(0,i)

print (b)

b = " ".join(b)


print (b)
