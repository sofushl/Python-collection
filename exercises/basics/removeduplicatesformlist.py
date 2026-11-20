import random

names = []
for i in range(0,50):
    n = random.randint(1,99)
    names.append(n)

names = set(names)
names = list(names)
print(names)
