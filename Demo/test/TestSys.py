import sys,os

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

print(dir(sys))

print("------------------")
print(sys.argv)

print("------------------")
print("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
print("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
print("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
print("os.path.abspath(__file__)=%s" % os.path.abspath(__file__))
print("os.getcwd()=%s" % os.getcwd())
print("sys.path[0]=%s" % sys.path[0])
print("sys.argv[0]=%s" % sys.argv[0])