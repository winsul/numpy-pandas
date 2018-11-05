import numpy as np

a = np.array([[1,2,3],[4,5,6]],dtype = np.int)
print(a)
'''定义array的type
包含了dtype，比如dtype= np.int
float, dtype= np.float
可选择16，32或者64位，int & float是做常用的
'''

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

a = np.zeros((3,5), dtype = int)
print('生成全部为0的矩,阵')
print(a)

a = np.ones((3,5))
print('生成全部为1的矩阵')
print(a)
print('blank')

a = np.empty((5,4))
print(a)
print('blank')

print('生成有序数列，有起始值，终止值，步长数，以及dtype类型')
print('类似range，包头不包尾，头是闭区间，尾是开区间')
a= np.arange(0,10,2,int)
print(a)

print('如果没设置后面的值，则逐个列出来')
a= np.arange(12)
print(a)

print('生成有一个有顺序的数列，shape可以自己定义，用reshape方法')
a = np.arange(15).reshape((3,5))
print(a)

print('将一段数分段，然后分布在数列中，也可以搭配reshape使用')
a = np.linspace(1,10,4)
print('为搭配reshape使用',a)
a = np.linspace(1,10,10,False, dtype=int).reshape((2,5))
print('搭配reshape使用',a)