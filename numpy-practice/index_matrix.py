import numpy as np

X = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
print(X[0]) #prints first row
print(X[3]) #prints last row 
print(X[0][0]) #prints first element on first row
print(X[3][3]) #prints last element on last row
print(X[1][1:3], X[2][1:3]) #Prints middle elements of middle rows
print(X[0][:2], X[1][:2]) #prints first two elements of first two rows
print(X[2][2:], X[3][2:]) #prints last two elements on last two rows