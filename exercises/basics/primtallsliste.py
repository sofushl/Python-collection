prime = [2]
num = 3

while num < 1000:
    num += 2
    print(f"___{num}")
    for i in prime:
        print(i)
        true = True
        if num%i == 0:
            true = False
            break
    if true == True:
        prime.append(num)

print (prime)
