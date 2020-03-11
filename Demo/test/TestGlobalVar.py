#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。

#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。


#列表可以修改，而字符串和元组不能。


# !/usr/bin/python3

total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)   #"0"


#当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
print("global---------------")
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()


#如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
print("nonlocal---------------")
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()



#以下程序执行，报错信息UnboundLocalError: local variable 'a' referenced before assignment
a = 10
def test():
    a = a + 1
    print(a)
test()
