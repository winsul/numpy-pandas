import numpy as np

a = np.arange(4)
print(a)

print('copy')
b = a
c = a
d = b
print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)
a[0]=100
print('a:',a)
print('b:',b)
print('c:',c)
print('d:',d)

print('deep copy')
b = a.copy()
a[0] = 200
print(a)
print(b)
# a与b并不指向同一个内存地址

