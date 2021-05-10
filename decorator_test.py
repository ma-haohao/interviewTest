'''
接收一个函数作为参数
可以有函数装饰器或者是类装饰器
'''
import time
def log_time(func):
    def _log(*args,**kwargs):
        beg=time.time()
        res=func(*args,**kwargs)
        print("user time: {}",format(time.time()-beg))
        return res
    return _log

@log_time
def test():
    return 1



class LogTime():
    def __init__(self,user_init=False):
        self.user_init=user_init
    def __call__(self, func):
        def _log(*args,**kwargs):
            beg=time.time()
            res=func(*args,**kwargs)
            if self.user_init==False:
                print("use time: {}", format(time.time()-beg))
            else:
                print("1")
            return res
        return _log

@LogTime(user_init=True)
def test2():
    print("test2")


if __name__ == '__main__':
    test2()
'''#闭包 closure
def outer(a,b):
    c=9
    def inner(x):
        res=(x-a+b)*c
        print(res)
        return res
    return inner

y=outer(5,6)
x=y(1)
print(x)'''

'''import time
def log_time(func):
    def _log(*args,**kwargs):
        beg=time.time()
        res=func(*args,**kwargs)
        print("user time:{}".format(time.time()-beg))
        return res
    return _log

class LogTime:
    def __init__(self,use_int=False):
        self.use_int=use_int

    def __call__(self, func):
        def _log(*args,**kargs):
            beg=time.time()
            res=func(*args,**kargs)
            if self.use_int:
                print("user time:{}".format(int(time.time() - beg)))
            else:
                print("user time:{}".format(time.time() - beg))
            return res
        return _log


@LogTime(use_int=True)
def mysleep():
    time.sleep(1)
    print('001')
    return 999

x=mysleep()
print(x)'''