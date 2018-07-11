import pandas as pd 
import matplotlib.pyplot as plt 

file = 'lsh_result.csv'
columns = ['index_col', 'file', 'rank']
results = pd.read_csv(file, header=None)
results.columns = columns
results = results.drop('index_col', axis=1)
summary = results['rank'].value_counts()
print(summary)
