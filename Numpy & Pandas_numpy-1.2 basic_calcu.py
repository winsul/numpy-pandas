import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.arange(5)

print('minus')
c = a-b
print(c)

print('plus')
c = a+b
print(c)

print('multi')
c = a*np.sin(b)
print(' 将值代入在进行计算也是可以得，一个一个代入')
print(c)

print('判断数字大小是否满足某个用户给的数字的条件，返回的是一个(伪)列表')
print(a < 30)
print(type(a < 30))

print('运算二维矩阵')
d = np.array([[1,2],[4,5]])
e = np.arange(4).reshape((2,2))
print(d)
print('blank')
print(e)
f = d*e
g = np.dot(d, e)
g_1 = d.dot(e)
'''逐个相乘就是位置上一一对应相称'''
print('逐个相乘', f)
print('矩阵乘法', g)

print('create a random array')
'''第二个random里面填入reshape的尺寸'''
a = np.random.random((2,6))
print(a)

print(np.sum(a))
print(np.min(a))
print(np.max(a))
'''
np.sum(a,axis=,dtype=)如果axis=0就是求列的和，
axis=1就是求行的和，其他函数情况类似
https://www.cnblogs.com/rrttp/p/8028421.html
'''


