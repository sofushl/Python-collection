t = int(input())

rødder = "1"

for i in range(2,t+1):
    if i**0.5%1==0:
        rødder += " " +  str(i)

print(rødder)