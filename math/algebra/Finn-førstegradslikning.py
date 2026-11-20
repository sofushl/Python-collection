ux1 = float(input("x1"))
uy1 = float(input("y1"))
ux2 = float(input("x2"))
uy2 = float(input("y2"))

if ux1 < ux2 or ux1 == ux2:
    x1 = ux1
    y1 = uy1
    x2 = ux2
    y2 = uy2
elif ux2 < ux1:
    x1 = ux2
    y1 = uy2
    x2 = ux1
    y2 = uy1

stt = (y2 - y1) / (x2 - x1) 
print (stt)
mx = x1
my = y1

while mx != 0:
    my = my - stt
    mx = mx - 1

print ('f(x) =', stt, '* x +', my)

