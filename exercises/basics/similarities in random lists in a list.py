import random

a = []
for i in range(0,50):
    n = random.randint(1,99)
    a.append(n)

b = []
for i in range(0,50):
    n = random.randint(1,99)
    b.append(n)

done = [x for x in a if x in b]
print (done)
