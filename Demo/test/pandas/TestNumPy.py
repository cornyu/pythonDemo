#numpy 中有两个重要的对象：ndarry 解决多维数组问题；ufunc 解决对数组进行处理的函数

import numpy as np
a = np.array([1,2,3])
b = np.array([[1,2,3],[2,3,4],[3,4,5]])
print('a.shape:', a.shape)
print('b.shape:', b.shape)

print('a.nbytes:', a.nbytes)
print('b.nbytes:', b.nbytes)

print('a.dtype:', a.dtype)
print('b.dtype:', b.dtype)
print('a:\n',a)
print('b:\n',b)


b[1,1]=100
print('b:\n',b)

print("----------结构数组-------------\n")
###结构数组
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']
})
peoples = np.array([("zhangsan", 18, 77, 99, 100),("lisi", 22, 79, 88, 90),("wangwu", 33, 66, 99, 99)], dtype=persontype)
print(peoples)

#获取所有age
ages = peoples[:]['age']
print(ages)

#求平均数
print(np.mean(ages))

print("-----------ufunc运算---------------\n")
x1 = np.arange(1, 11, 2) #创建等差数组
x2 = np.linspace (1, 9, 5) #创建等差数组
print(x1)#[1 3 5 7 9]
print(x2)#[1. 3. 5. 7. 9.]

x3 = np.add(x1,x2)
print(x3) #[ 2.  6. 10. 14. 18.]

x4 = np.subtract(x1, x2)
print(x4) #[0. 0. 0. 0. 0.]

x5 = np.multiply(x1,x2)
print(x5) #[ 1.  9. 25. 49. 81.]

x6 = np.divide(x1,x2)
print(x6) #[1. 1. 1. 1. 1.]

print("----------- 统计函数---------------\n")
aa = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(aa)) #最小值 1
print(np.amin(aa, 0)) #[1 2 3]
print(np.amin(aa, 1)) #[1 4 7]

print(np.amax(aa))  #最大值 9
print(np.amax(aa, 0))  #[7 8 9]
print(np.amax(aa, 1))  #[3 6 9]

print("---------最大值和最小值")
print(np.ptp(aa)) # 最大值和最小值的差 9-1=8
print(np.ptp(aa, 0)) #[6 6 6]
print(np.ptp(aa, 1)) #[2 2 2]

print("---------求平均数")
print(np.mean(aa)) #5.0
print(np.mean(aa, 0)) #[4. 5. 6.]
print(np.mean(aa, 1)) #[2. 5. 8.]

print("---------加权平均值")
bb = np.array([1, 2, 3, 4])
print(np.average(bb))   # (1+2+3+4)/4 = 2.5
wts = np.array([1, 2, 3, 4])
print(np.average(bb, weights=wts))  # (1*1 + 2*2 + 3*3 + 4*4)/(1+2+3+4) = 3.0

print("---------标准差，方差")
print(np.std(bb))   #标准差  1.118033988749895
print(np.var(bb))   #方差 1.25


print("---------排序")
# 4,3,2
# 2,4,1

cc = np.array([[4, 3, 2],[2, 4, 1]])
print(np.sort(cc))
# [[2 3 4]
#  [1 2 4]]
print(np.sort(cc, axis=None)) # [1 2 2 3 4 4]
print(np.sort(cc, axis=0))
# [[2 3 1]
#  [4 4 2]]
print(np.sort(cc, axis=1))
# [[2 3 4]
#  [1 2 4]]

print("----------cmp函数")

print("----------lambda")

#print(np.ones(10, 5))


