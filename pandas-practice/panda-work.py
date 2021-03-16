import numpy as np
import pandas as pd

pd.Series([], dtype='float')

X = ['A','B','C']
print(X, type(X))
Y = pd.Series(X)
print(Y, type(Y))