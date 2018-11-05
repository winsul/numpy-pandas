import numpy as np

a = np.arange(1,4,1)
b = np.arange(101,104,1)

'''纵向合并'''
c = np.vstack((a,b)) #vertical stack
print(c)

'''横向合并'''
c = np.hstack((a,b)) #horizontal stack
print(c)

print('from horizontal to vertical')
c = a.reshape(3,1)
print(c)
print('another way')
print(a[:,np.newaxis])
print(a)

print('自主选择合并的方向')
# np.concatenate()
a = np.array([1,2,3])[:,np.newaxis]
b = np.array([4,5,6])[:,np.newaxis]
c = np.concatenate((a,b,b,a),axis=1)
print(c)
c = np.concatenate((a,b,b,a),axis=0)
print(c)

