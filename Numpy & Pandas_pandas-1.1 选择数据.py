import numpy as np
import pandas as pd

dates = pd.date_range('20180908',periods=6)
df = pd.DataFrame(np.arange(0,24,1).reshape((6,4)), index = dates, columns = ['a','b','c','d'])
print(df)

print('select a specific column or row')
print(df['a'])
print(df.a)
print(df[0:1])
print(df['20180908':'20180910'])
print('纯标签搜索select by label: loc[index索引, col列索引[]')
print(df.loc['20180909'])

print(df.loc[:,['a','b']])
print(df.loc['20180909',['a','b','c']])

print('纯数字搜索selectd by position: iloc')
print(df.iloc[3])
print(df.iloc[3, 1:3])#第3行数据的第一个到第二个的数据，从零开始技计数
print(df.iloc[[1, 3, 5], [1, 3]])

print('mixed select混合了标签和数字的搜索')
print(df.ix[[0,2,4],'a':'c'])
print(df.ix['20180908':'20180912',['a','c']])

print('boolean indexing')
print(df.a)
print(df[df.a>6])