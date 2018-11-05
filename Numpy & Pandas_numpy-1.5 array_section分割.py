import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

print('横向分割-按行分割')
b = np.split(a,3,axis = 0)
print(b)

print('横向分割-按列分割')
b = np.split(a,2,axis = 1)
print(b)

print('不等量分割')
b = np.array_split(a,3,axis = 1)
print(b)

print('vsplit')
# vertical split 就是沿着x轴方向，切过y轴
b = np.vsplit(a,3)
print(b)

print('hsplit')
b = np.hsplit(a,2)
print(b)

