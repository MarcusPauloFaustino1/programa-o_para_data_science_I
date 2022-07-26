import numpy as np 

a = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])

a = a.reshape(1,-1)

print(a)
