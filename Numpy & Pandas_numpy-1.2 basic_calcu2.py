import numpy as np

a = np.arange(2,14).reshape(3,4)
print(a)
print('search the minum in the array')
b = np.argmin(a)
print(b)

print('search the maxim in the array')
b = np.argmax(a)
print(b)

print('calculate the mean in three ways')
b = np.mean(a)
print(b)
b = a.mean()
print(b)
b = np.average(a)
print(b)

print('calculate the medium')
b = np.median(a)
print(b)

print('accumulate the array number step by step in a list')
b = np.cumsum(a)
print(b)

print('display the differs with the former number')
b = np.diff(a)
print(b)

print('find the nonzero')
c = np.array([[0,0,0],[9,3,0],[1,2,3]])
print(c)
b = np.nonzero(c)
'''row-col'''
print(b)

print('排序')
b = np.sort(c)
print(c)
print(b)
'''在行内排序，而非整个array排序'''

print('矩阵的转置，类似于矩阵A.T,矩阵内行列对换')
b= np.transpose(a)
print(a)
print(b)
print(a.T)
print('矩阵的倒置和原矩阵的相乘')
print(a.T.dot(a))

print('截取array里面的数')
'''
clip里面需要填3个参数
第一个选定需要截取的array
第二个，第三个确定范围(min,max)
输出的array里面，小于min的全部变为min
大于max的泉币变为max
'''
b = np.clip(a,4,12)
print(b)
