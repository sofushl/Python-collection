#definerer funskjonen
def f(x):
    return x^2

#bestemmer verdiene som utregningen skal bruke
n = 1000
a = 1
b = 10
dx = (b-a)/n

#integralmetodebibliotek
integralmet = {
    "rect": lambda dx,f,a,i,p: dx*f(a+(i+1-p)*dx),
    "trap": lambda dx,f,a,i,p: (f(a+i*dx)+f(a+(i+1)*dx))*dx/2
}

#Utregning
def integralrek(a, b, n, f, meth, p=0, i=0):
    dx = (b-a)/(n)

    if i==n-1:
        return integralmet[meth](dx,f,a,i,p)
    else:
        return integralmet[meth](dx,f,a,i,p) + integral(a, b, n, f, meth, p, i+1)
    
def integral(a, b, n, f, meth, p=0, i=0):
    dx = (b-a)/(n)
    F=0
    for i in range(n):
        F += integralmet[meth](dx,f,a,i,p)
    return F



print(round(integral(a,b,n,f,"rect",0),2))
print(round(integral(a,b,n,f,"rect",1),2))
print(round(integral(a,b,n,f,"rect",0.5),2))
print(round(integral(a,b,n,f,"trap"),2))
