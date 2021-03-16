import numpy as np

a = [-5, -3, 0, 10, 40]
a= np.asfarray(a) #changes element types to floats

b = [-5, -3, 0, 10, 40]
b=np.flip(b) #reverses order of b

c = np.zeros(10) #creates array of zeros
print(f'Before: {c}') #outputs array
c[4]=1 #changes fifth element
print(f'After: {c}') #outputs changed array