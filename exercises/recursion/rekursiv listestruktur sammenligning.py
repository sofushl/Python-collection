a = eval(input())
b = eval(input())

def fun(a,b):
    #print(type(a),type(b))
    try:
        if type(a) != type(b):
            return False
        elif type(a) == list:
            for i in range(len(a)):
                if fun(a[i],b[i])==False:
                    return False
    except:
        return False
        
if fun(a,b) == False:
    ans = False
else:
    ans = True
        
print(ans)

        
