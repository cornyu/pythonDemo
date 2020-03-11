# -*- coding: utf-8 -*-
import getpass

# 除法
print(20/3)


name = "alex"
print("i am %s " % name)
#exit(0)


#将用户输入的内容赋值给 name 变量
name = input('What is your name?')
#打印输入的内容
print('Hello',name)


# 将用户输入的内容赋值给 pwd 变量
pwd = getpass.getpass("请输入密码：")
# 打印输入的内容
print(pwd)

