import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

print('series线图')
data = pd.Series(np.random.randn(1000),index = np.arange(1000))
data = data.cumsum()
data.plot()
plt.show()

print('\nDataFrame类矩阵')
data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
print(data)
data = data.cumsum()
#print(data.head()) # 默认输出前五个数据
data.plot()
plt.show