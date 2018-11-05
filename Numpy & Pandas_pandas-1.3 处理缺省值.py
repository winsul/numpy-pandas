import pandas as pd
import numpy as np

dates = pd.date_range('20180916',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates, columns = ['A','B','C','D'])

df.iloc[0,0] = np.nan
df.iloc[2,3] = np.nan
print(df)

'直接不要有nan的整一行'
print(df.dropna())
'axis = 0丢掉行'
print(df.dropna(axis = 0, how = 'any'))#'how = {['any','all']}'
#出现how = 'all'的情况是，需要整行都是nan才会被drop

print(df.fillna(value = 19920928))

'判别表里是否有nan'
print(df.isna())

print(np.any(df.isnull() == True))