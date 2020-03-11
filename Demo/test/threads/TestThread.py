from threading import  Thread
from multiprocessing import  Process
from timeit import  timeit

#计算密集型任务
def  count( n ):
     while n > 0:
        n -= 1


#不采用多任务模式
def test_normal():
    count(10000)
    count(10000)


#多线程
def test_thread():
    t1 = Thread(target=count, args=(100000,))
    t2 = Thread(target=count, args=(100000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

#多进程方式
def test_process():
    p1 = Process(target=count, args=(100000,))
    p2 = Process(target=count, args=(100000,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    print('__main__')
    print(timeit('test_normal()', 'from __main__ import test_normal', number=10))
    print(timeit('test_thread()', 'from __main__ import test_thread', number=10))
    print(timeit('test_process()', 'from __main__ import test_process', number=10))