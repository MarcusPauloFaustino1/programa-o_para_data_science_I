import numpy as np 

a = np.arange(10).reshape(2,-1)
b = np.repeat(1,10). reshape(2,-1)

c = np.concatenate((a,b))

print(c)
