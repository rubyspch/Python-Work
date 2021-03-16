import numpy as np

a = [-5, -3, 0, 10, 40]
a= np.asfarray(a) #changes element types to floats

b = [-5, -3, 0, 10, 40]
b=np.flip(b) #reverses order of b

c = np.zeros(10) #creates array of zeros
print(f'Before: {c}') #outputs array
c[4]=1 #changes fifth element
print(f'After: {c}') #outputs changed array

d = np.array([10, 20, 30, 50]) #creates array
d[3]=40 #changes last element

e = np.array([ #create array e
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
e[3]=[1,1,1,1] #change last row to all ones
e[3][3]=0 #change last element to 0
e += 5 #adds 5 to every element