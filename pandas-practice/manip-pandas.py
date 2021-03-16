import numpy as np
import pandas as pd

X = pd.Series([4,2,5,1,3],
              index=['fourth','second','fifth','first','third'], dtype='int64')
print(X)
X=X.sort_values() #sorts values to ascending order
print(X)
X=X.astype('float64') #converts X elements to floats
X[4]=10 #sets fifth element to 10
print(X)
X['second':'fourth']=0 #sets middle values to 0
print(X)
X+=5 #adds 5 to all elements
print(X)