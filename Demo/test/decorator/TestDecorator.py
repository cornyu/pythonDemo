# 装饰器，在不改变函数代码情况下，给函数增加新的功能

def log(func):
    def wrapper(*args, **kw):
        print('output %s():' %func.__name__)
        return func(*args,**kw)

    return wrapper

@log
def Stock_600213(Close):
    print('2019-04-16 {} :6.54'.format(Close))


Stock_600213('Open')