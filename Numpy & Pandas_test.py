import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.ones((3, 4))*0, columns = ['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3, 4))*0, columns = ['a','b','c','e'], index=[1,2,3])

ret = pd.concat([df1,df2])
print(ret)