l = [1,4,6,7,9,3,4,6,2,7,7,2,9,0,9,0,1,4,4,3]

l.sort()

avg = float(sum(l)/len(l))

med = float(l[int(len(l)/2)] if (len(l)/2)%2==0 else (l[int(len(l)/2+0.5)]+l[int(len(l)/2-0.5)])/2)

print(len(l))
print(l)
print(med,avg)