# coding:utf-8
from multiprocessing import Process, Pipe

def func(conn2):
    conn2.send("I am child process")
    print("message from father side: ",conn2.recv())
    conn2.close()

if __name__ == '__main__':
    conn1,conn2=Pipe()
    p=Process(target=func,args=(conn2,))
    p.start()
    print("messgae from child side: ",conn1.recv())
    conn1.send("I am father process")
    conn1.close()
