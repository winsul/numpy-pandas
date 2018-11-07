import pandas as pd
import numpy as np

# merging two df by key/keys.
print('ordinary')
left = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'a': ['a0', 'a1', 'a2', 'a3'],
                     'b': ['b0', 'b1', 'b2', 'b3']})

right = pd.DataFrame({'key': ['k0', 'k1', 'k2', 'k3'],
                     'c': ['c0', 'c1', 'c2', 'c3'],
                     'd': ['d0', 'd1', 'd2', 'd3']})

ret = pd.merge(left, right, on= 'key')
print(left)
print(right)
print(ret)

# 根据两个keys合并df
print('\n two keys')
left = pd.DataFrame({'key': ['k0', 'k0', 'k1', 'k2'],
                     'key1': ['k0', 'k1', 'k0', 'k1'],
                     'a': ['a0', 'a1', 'a2', 'a3'],
                     'b': ['b0', 'b1', 'b2', 'b3']})

right = pd.DataFrame({'key': ['k0', 'k1', 'k1', 'k2'],
                      'key1': ['k0', 'k0', 'k0', 'k0'],
                     'c': ['c0', 'c1', 'c2', 'c3'],
                     'd': ['d0', 'd1', 'd2', 'd3']})

ret = pd.merge(left, right, on=['key', 'key1'])
# merge默认是inner,,how = 'inner',  concat默认是outer
# how = ['left', 'right', 'inner', 'outer']
print(left)
print(right)
print(ret)

# indicator
print('\n indicator')
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1)
print(df2)
ret = pd.merge(df1, df2, on='col1', how='outer', indicator=True)
print(ret)

# index
print('\n index')
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

print(left)
print(right)
ret = pd.merge(left, right, left_index = True, right_index = True, how = 'outer')
ret1 = pd.merge(left, right, left_index = True, right_index = True, how = 'inner')
print(ret)
print(ret1)


print('\n overlap')
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
ret = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')
print(boys)
print(girls)
print(ret)

