import numpy as np

a = np.arange(3,21)
print(a[3])

print('row index')
a = np.arange(3,21).reshape(3,6)
print(a[2])

print('col index')
'''：表示所有的数'''
a = np.arange(3,21).reshape(3,6)
print(a[:,2])
'''a[:,2]表示所有的行的第二列'''


print('row-col index')
a = np.arange(3,21).reshape(3,6)
print(a[2][2])
print(a[2,2])


print('output row')
for row in a:
    print(row)

print('output col')
for col in a.T:
    print(col)
print('blank')
for col in np.transpose(a):
    print(col)

print('将一个矩阵所有的item放在一行中')
print(a.flatten())

print('output every item')
for i in a.flat:
    print(i)
