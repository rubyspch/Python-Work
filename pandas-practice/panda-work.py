import numpy as np
import pandas as pd

pd.Series([], dtype='float')

X = ['A','B','C'] #create python list
print(X, type(X))
Y = pd.Series(X) #convert python list X to pandas series Y
print(Y, type(Y))
Y.name='My letters'
print(Y.values)