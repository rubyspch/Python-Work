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
print(f'e={e}') #create array of ones and prints with string literal

f=np.repeat(5,16).reshape(4,4) #repeats 5 16 times, and reshapes elements into 4 rows and 4 columns
print(f)

g=np.repeat(7,4).reshape(2,2)
h=np.full((2,2),7) #creates 2*2 matrix and fills it with 7s

print(g)
print(h)

i=np.eye(3,3) #creates matrix with disgonal 1s and the rest as 0s
print(i)