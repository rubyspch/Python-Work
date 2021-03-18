import numpy as np

a = np.array([-1,2,0,-4,5,6,0,0,-9,10])

b= a[a<0] #assigns elements in a that are less than 0 to b
print(b)

c = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(c[c>5]) #prints values in c that are greater than 5

d = np.array([-1, 2, 0, -4, 5, 6, 0, 0, -9, 10])
print(d[d>d.mean()])