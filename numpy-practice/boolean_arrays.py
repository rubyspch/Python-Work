import numpy as np

a = np.array([-1,2,0,-4,5,6,0,0,-9,10])

b= a[a<0] #assigns elements in a that are less than 0 to b
print(b)

print(a[a>5]) #prints values in a that are greater than 5

print(a[a>a.mean()]) #prints mean of a

print(a[(a==2)|(a==10)]) #prints elements equal to 2 or 10