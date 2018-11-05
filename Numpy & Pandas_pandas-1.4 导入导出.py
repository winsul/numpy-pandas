import numpy as np
import pandas as pd

data = pd.read_csv('test1_csv.csv')
print(data)

data.to_csv('test2_csv.csv')