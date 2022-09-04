# -*- coding: utf-8 -*
'''
这是多行注释，用三个单引号
这是多行注释，用三个单引号
这是多行注释，用三个单引号
'''


while True:
       try:
              inputValue = input('输入两个数字，以空格隔开')
              a = inputValue.split()
              print(int(a[0]) + int(a[1]))
       except:
              break
              exit(0)


