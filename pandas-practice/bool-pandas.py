import numpy as np
import pandas as pd

X = pd.Series([-1,2,0,-4,5,6,0,0,-9,10])
X_mask=X<0 #creates boolean mask showing values less than 0
print(X_mask)
Y=X[X_mask] #Applies mask to X and places it inside Y. Creates new series with values from X that meet the X_mask condition
print(Y) 

print(X[X>5]) #prints elements in X over 5

print(X[X>X.mean()]) #prints series of elements in X over the mean

condition=(X==2) | (X==10) #create condition for series
print(X[condition]) #applies condition to X and prints elements that are True
