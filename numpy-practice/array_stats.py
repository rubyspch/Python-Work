import numpy as np

X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])

print(sum(X)) #prints sum
print(X.sum()) #prints sum
print(X.mean()) #prints mean
print(print(np.amax(X))) #prints max

Y = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

print(np.sum(Y, axis=0)) #prints sums of columns (axis 0)
print(np.mean(Y, axis=1)) #prints mean averages of rows