import numpy as np
import pandas as pd

X = pd.Series([1,2,3,4,5],
              index=['forth','second','fifth','first','third'], dtype='int64')
print(X)
X.sort_values(ascending=True)
X=X.astype('float64') #converts X elements to floats
print(X)

