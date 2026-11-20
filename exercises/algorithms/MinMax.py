liste = list(map(int, input().split()))

min = 1000
max = -1000


for i in liste:
    if i < min:
        min = i
    if i > max:
        max = i


print(min)
print(max)