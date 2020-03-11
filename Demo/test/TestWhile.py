#!/usr/bin/python3
# -*- coding: utf-8 -*-



condition = 1
while condition < 10:
    print(condition)
    condition += 1   # 相当于 condition = condition + 1


print("----------------------")
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")



print("----------------------")
for i in range(5,9) :
    print(i)


print("----------------------")

a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])


print("pass----------------------")
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")