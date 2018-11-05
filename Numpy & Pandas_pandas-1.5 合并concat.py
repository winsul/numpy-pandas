import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['a','b','c','d'])

# concatencating
ret = pd.concat([df1,df2,df3],axis = 0, ignore_index= True)
print(ret)

# join, ['inner', 'outer']
df1 = pd.DataFrame(np.ones((3, 4))*0, columns = ['a', 'b','c','d'],index = [1,2,3])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns = ['d', 'a','b','e'],index = [2,3,4])

ret = pd.concat([df1, df2], join = 'inner', ignore_index = True)
print(ret)

# default
print('default')
ret = pd.concat([df1, df2], join = 'outer')
print(ret)

# join_axes
df1 = pd.DataFrame(np.ones((3, 4))*0, columns = ['a', 'b','c','d'],index = [1,2,3])
df2 = pd.DataFrame(np.ones((3, 4))*1, columns = ['d', 'a','b','e'],index = [2,3,4])
ret = pd.concat([df1, df2], axis=1)
print(ret)

ret = pd.concat([df1,df2], axis = 1, join_axes=[df1.index])
print(ret)


# append
print('append')
df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['b','c','d','e'], index = [2,3,4])

ret = df1.append(df2, ignore_index = True)
ret1 = df1.append([df2,df3])

print(ret)
print(ret1)

s1 = pd.Series([1,2,3,4], index = ['a','b','c','d'])
ret2 = df1.append(s1,ignore_index = True)
print(ret2)