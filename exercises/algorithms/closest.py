n = int(input())
k = int(input())
s,t = input().split()
s = int(s)
t = int(t)
punkter = []
for i in range(n):
    x,y = input().split()
    punkter.append((int(x),int(y)))

distances = []

for i in punkter:
    distances.append( ( (i[0]-s)**2 + (i[1]-t)**2 )**0.5 )

closest = []

for i in range(k):
    min = distances[0]
    mini = 0
    for i in range(len(punkter)):
        if distances[i] < min:
            min = distances[i]
            mini = i
    closest.append(punkter[mini])
    del punkter[mini]
    del distances[mini]

for i in closest:
    print(i[0],i[1])