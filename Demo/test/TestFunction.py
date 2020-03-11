#!/usr/bin/python3

# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome", name)


print_welcome("yujinyu")
w = 4
h = 5
print("width =", w, " height =", h, " area =", area(w, h))


#实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，
# 在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。
def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print(b)  # 结果是 2



#可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。例如：
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值: ", mylist)
    return

# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值: ", mylist)


print("不定长参数------------------")
#不定长参数
#你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

#def functionname([formal_args,] *var_args_tuple ):
#   "函数_文档字符串"
#   function_suite
#   return [expression]
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)
printinfo( 10 )  #如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量


#加了两个星号 ** 的参数会以字典的形式导入。
def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)

# 调用printinfo 函数
printinfo(1, a=2, b=3)





