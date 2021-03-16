import numpy as np
import pandas as pd

pd.Series([], dtype='float')

X = ['A','B','C'] #create python list
print(X, type(X))
Y = pd.Series(X) #convert python list X to pandas series Y
print(Y, type(Y))
Y.name='My letters' #gives series a name
print(Y.values) #prints the series values

index_names = ['first', 'second', 'third'] 
Y.index=index_names #adds list of strings to series as index names
print(Y['first']) #prints element with index first
print(Y['third']) #prints element with index third

Z = pd.Series(['A','B','C','D','E'],
              index=['first','second','third','fourth','fifth']) #creates new series Z with specified index names
print(Z['second':'fourth']) #prints middle elements
print(Z[['first','fifth']]) #prints first and fifth elements
print(Z.sort_values(ascending=False)) #prints values in reverse order