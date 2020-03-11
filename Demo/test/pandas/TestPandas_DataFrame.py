#DataFrame 是个表格数据型的数据结构，既有行索引也有列索引，创建的方式一般维：
# pd.DataFrame(data, index = index, column = columns )

import pandas as pd
from pandas import Series, DataFrame

data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
print('data dict:\n',data)

df1 = DataFrame(data)
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print('df1:\n',df1)
print('df2:\n',df2)

df3 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
print('df3 describe:\n',df3.describe())

print("----- 数据合并------\n")
df4 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df5 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
print('df4:\n', df4)

print('df5:\n', df5)

#将name的值相同的 合并到一个
df6 = pd.merge(df4, df5, on='name')
print('df6:\n',df6)
print("\n")

df7 = pd.merge(df4, df5, how='inner')
print('df7:\n',df7)


df8 = pd.merge(df4, df5, how='left')
print('df8:\n', df8)


#两个 进行合并
df9 = pd.merge(df4, df5, how='outer')
print('df9:\n', df9)
