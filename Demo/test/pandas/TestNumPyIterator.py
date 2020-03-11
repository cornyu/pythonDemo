#numpy 中有两个重要的对象：ndarry 解决多维数组问题；ufunc 解决对数组进行处理的函数

import numpy as np

x = [1,2,3]
its = x.__iter__()
# 结果 <list_iterator object at 0x103bac160>
print(its)

print(next(its)) #输出1
print(next(its)) #输出2
print(next(its)) #输出3


class MyRange:
    def __init__(self, num):
        self.i = 0
        self.num = num

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.num:
                i = self.i
                self.i += 1
                return i
            else:
                raise StopIteration()



#for i in MyRange(10):
#	print(i)

##生成器函数方式实现生成器
def gensquares(N):
	for i in range(N):
		yield i**2

#<generator object gensquares at 0x1037946d0>
print(gensquares(5))

for i in gensquares(5):
	print(i)


#生成器表达式方式实现生成器
print(x**2 for x in range(5))
print(list(x**2 for x in range(5)))

#源代码 见 https://github.com/yuanxiao1/Python-Quantitative-Trading/tree/master/Chapter12
