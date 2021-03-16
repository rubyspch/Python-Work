import numpy as np
import pandas as pd

pd.Series([], dtype='float')

X = ['A','B','C'] #create python list
print(X, type(X))
Y = pd.Series(X) #convert python list X to pandas series Y
print(Y, type(Y))
Y.name='My letters'
print(Y.values)

index_names = ['first', 'second', 'third'] 
Y.index=index_names #adds list of strings to series as index names
print(Y['first']) #prints element with index first
print(Y['third']) #prints element with index third 