num = int(input("provide a number"))

prime = [2]
pnum = 2
facto = []

while pnum < num:
    pnum += 1
    for i in prime:
        print(i, "___", pnum)
        true = True
        if pnum%i == 0:
            true = False
            break
    if true == True:
        prime.append(pnum)

print (prime)


while not num in prime:
    for i in prime:
        if num % i == 0:
            facto.append(i)
            num = num/i
            print (str(num) + "/" + str(i))
            break

facto.append(num)
print (facto)
