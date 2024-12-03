import numpy as np
import pandas as pd


df = pd.read_csv(r'C:\01-real.txt', delimiter='   ', header=None)

first_column = df[0]  
second_column = df[1]

array1 = np.array(first_column.sort_values())
array2 = np.array(second_column.sort_values())

print (abs(array1-array2).sum())