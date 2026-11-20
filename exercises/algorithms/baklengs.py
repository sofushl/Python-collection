s = ([*str(input())])

b = []

for i in s[::-1]:
    b.append(i)

b = ''.join(b)

print(b)