import pandas as pd
import numpy as np

s = pd.Series([1,3,6,np.nan,8,11])
print(s)

print('定义index')
dates = pd.date_range('20180101',periods = 6)
print(dates)

print('类似定义一个array，但是可以定义纵横坐标的index')
print('行的索引是index，列的索引的columns')
df = pd.DataFrame(np.random.rand(6,4),index = dates,columns = ['a','b','c','d'])
print(df)
print('pandas默认也会给出纵横坐标的索引标签，都是从0开始标号')

# numpy.random.randn(d0, d1, …, dn)是从标准正态分布中返回一个或多个样本值。
# numpy.random.rand(d0, d1, …, dn)的随机样本位于[0, 1)中。

print('也可以用嵌入字典的方式做索引标签')
df = pd.DataFrame({'a':pd.Series(1,index = list(range(4))),
                   'b':['abc','bbc','cnn','nhk'],
                   'c':pd.Timestamp('20180905'),
                   'd':pd.Categorical(['abc','nhk','bbc','nyt'])})
print(df)
print('每一行数据的类型')
print(df.dtypes)
print('输出行列索引标签的类型')
print(df.index)
print(df.columns)

print('输出列表中的每一行数据')
print(df.values)
import time
for i in df.values:
    print(i)
    time.sleep(0.2)

print('做一个基本的统计')
print('会默认去除文本类型以及类似的类型，保留int之类的类型')
print(df.describe())

print('pandas里的矩阵转置')
print(df.T)

print('排序 根据index sort')
print('按列排序')
print(df.sort_index(axis = 1,ascending=False))
print('按行排序')
print(df.sort_index(axis = 0,ascending=False))

print('对值进行排序(根据某一行的数据，对整张表排序)')
print(df.sort_values(by = 'd',ascending=False))
