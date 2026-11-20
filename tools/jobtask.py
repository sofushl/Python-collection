
def find(num):
    
    n = 0 
    
    while num != 0:
        n+=1
        print(num, end=" ")
        if num%2 != 0:
            num-=1
        else:
            num=int(num/2)
        
    return n



if __name__ == "__main__nu":
    for i in range(1,20):
        print("Next = " + str(i))

        print("\nResult = " + str(find(i)))

print(find(144))