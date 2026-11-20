import numpy as np




def Convolute(I: list, K: list, padding = 0, stride = 1, padtype: str = "0"):
    Io = []

    if padding > 0:
        if padtype == "0":
            for i in range(np.shape(I)[0]):
                for j in range(padding):
                    I[i].append(0)
                    I[i].insert(0,0)
            l = []
            for i in range(np.shape(I)[1]):
                l.append(0)
            for i in range(padding):
                I.append(l)
                I.insert(0,l) 



    for i in range(int(np.shape(I)[0]/stride -(np.shape(K)[0]-stride)/stride)):
        l = []
        for j in range(int(np.shape(I)[1]/stride-(np.shape(K)[1]-stride)/stride)):
            sum = 0
            for n in range(np.shape(K)[0]):
                for m in range(np.shape(K)[1]):
                    sum+= K[n][m] * I[n+(i*stride)][m+(j*stride)]
            l.append(sum)
        Io.append(l)
    return Io

print(Convolute(
    [[9, 1],
           [7, 3]]  
    ,
    [[1, 0, -1],
           [1, 0, -1],
           [1, 0, -1]]
    ,
    2,2

))[1][1] = 7