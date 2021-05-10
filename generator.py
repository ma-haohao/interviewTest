'''#yield 生成器
#例1，斐波那契数列
def fibonacci(n):
    a,b=0,1
    while b<n:
        a,b=b,a+b
        yield a
f=fibonacci(100)
#例2，inspect来查看协程的当前状态
import inspect'''
#使用装饰器实现协程的预激活
from functools import wraps
def coroutine(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
'''@coroutine
def generator():
    l=[]
    while True:
        value=yield
        if value=='CLOSE':
            break
        l.append(value)
    return l

g=generator()
g.send("test")
inspect.getgeneratorstate(g)
g.throw(ValueError)
g.close()
inspect.getgeneratorstate(g)



print(next(f))
print(next(f))
print(next(f))'''

#yield from 的应用实例
def average_gen():
    total=0
    count=0
    average=0
    while True:
        new_num=yield average
        if new_num is None:
            break
        count+=1
        total+=new_num
        average=total/count
    return total,count,average

#委托生成器
@coroutine
def proxy_gen():
    while True:
        total,count,average=yield from average_gen()
        print("计算完毕！\n总共传入{}个数值，总和：{}，平均数：{}".format(count,total,average))

def main():
    cal_average=proxy_gen()
    print(cal_average.send(10))
    print(cal_average.send(20))
    print(cal_average.send(30))
    cal_average.send(None) #结束协程

if __name__ == '__main__':
    main()