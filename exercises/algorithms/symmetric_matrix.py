import numpy as np

symmat = np.matrix([[1,2,1],
                    [2,1,2],
                    [1,2,1]])

asymmat = np.matrix([[1,2,3],
                     [4,5,6],
                     [7,8,9]])

A = symmat

At = np.transpose(A)


sym = True

for i in range(np.shape(A)[0]):
    for j in range(np.shape(A)[1]):
        if A[i,j] != At[i,j]:
            sym = False
            break

if sym:
    print("symmetrisk")
else:
    print("asymmetrisk")