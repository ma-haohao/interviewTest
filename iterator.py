#codin=uft-8

class Mylist(): #可迭代对象
    def __init__(self,num):
        self.data=num #上边界

    def __iter__(self):
        return MyListIterator(self.data) #返回该可迭代对象的迭代器实例

class MyListIterator():  #定义迭代器类，其是MyList可迭代对象的迭代器类
    def __init__(self,data):
        self.data=data #上边界
        self.now=0 #当前迭代值

    def __iter__(self):
        return self #返回该对象的迭代器类的实例；因为自己就是迭代器，所以就返回self

    def __next__(self):
        while self.now<self.data:
            self.now+=1
            return self.now-1
        raise StopIteration

#当函数里面有一个yield就成了生成器函数
def simple_gen():
    yield 'hello'
    yield 'world'

gen=simple_gen()
print(gen)
print(next(gen))
print(next(gen))

my_list1=MyListIterator(5)
print(type(my_list1))
print(next(my_list1))
print(my_list1.now)
print(next(my_list1))
print(my_list1.now)

my_list2=Mylist(5)
for i in my_list2:
    print(i)

def coro():
    hello=yield 'hello'
    yield hello
c=coro()
print(next(c))
print(c.send('world'))

l=[5,30,3,4,7]
x=sorted(l)
print(x)