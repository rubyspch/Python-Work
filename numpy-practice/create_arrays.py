import numpy as np
a=np.array([0,0,0,0,0,0,0])
print(a.size) # prints number of elements in array

b=np.arange(10,50) #adds numbers 10-49 to array
print(b) 

c=np.array([[1,1],[1,1]])
print(c.shape) #outputs shape of matrix (2,2)

d=np.array([[1,1], [1,1], [1,1]])
d=d.astype(np.float) #changes type of elements to float
print(d)

e=np.repeat(1,5)
print(f'e={e}')

f=np.repeat(5,16).reshape(4,4)
print(f)
