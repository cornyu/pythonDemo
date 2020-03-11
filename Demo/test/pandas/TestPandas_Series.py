#Serias 类似于一维数组，基本方法：s = pd.Series(data, index = index),其中的data可以是list,ndarray这样的阵列组成的一维数组，也可以是长量和字典组成的一维数组

import pandas as pd
import numpy as np


from pandas import Series, DataFrame
x1 = Series([1,2,3,4])
x2 = Series(data=[1,2,3,4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
# a    1
# b    2
# c    3
# d    4
#dtype: int64

#dtype: int64 显示的是数据类型

d = {'a': 1, 'b': 2, 'c': 3}
x3 = Series(d)
print('x3:\n', x3)

x4 = Series(d, index=['b','c','d'])
print('x4:\n', x4)


s = pd.Series([0.8888765, 1234, 21.445, 129], index=['a', 'b', 'c', 'd'], dtype = 'float')
print('s:\n', s)

#以ndarray作为数据类型创建一个Series对象
nprandom = pd.Series(np.random.rand(5))
print('nprandom:\n', nprandom)

print('\nSeries数据对象的访问')
#Series数据对象的访问
print('nprandom.values:\n', nprandom.values)

print('nprandom.index:\n', nprandom.index)