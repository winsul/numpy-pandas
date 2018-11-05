import pandas as pd
import numpy as np

dates = pd.date_range('20180916',periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index = dates, columns = ['A','B','C','D'])

df.iloc[2,2] = 19920928
df.loc['20180919','D'] = 'hmq'

print(df)


df[df.B>9] = 1314
print(df)

df.B[df.B > 9] = 9999
print(df)

'直接定义一列'
df['M'] = [1,2,3,4,5,6]
print(df)
df['H'] = pd.Series([6,5,4,3,2,1], index = pd.date_range('20180916',periods = 6))
print(df)