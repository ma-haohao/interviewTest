def print_multiple_args(*args,**kargs):
    print(type(args),args)
    for idx,val in enumerate(args):
        print(idx,val)

def hello(name:str)->str:
    return 'hello'+name

def clear_list(l):
    l=[]
def flist(l=[]):
    l.append(1)
    print(l)
flist()
flist()

ll=[1,2,3]
clear_list(ll)
print(ll)
#print(range(10))

from queue import Queue

q=Queue(maxsize=5)
for i in range(5):
    q.put(i)
print(q.get())
q.put(10)
while q.empty()==False:
    q.get()