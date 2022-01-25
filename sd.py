import pandas as pd
import numpy as np
import csv

#pandas.read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, ....)
df = pd.read_csv('zif82.csv', sep= ' ')

#print(df)
#print(df.to_string())
print(df.std())
#print(df['Density'].std())
