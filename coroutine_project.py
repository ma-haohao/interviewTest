'''import time
import redis
import asyncio
from queue import Queue
from threading import Thread

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def do_sleep(x,queue):
    await asyncio.sleep(x)
    queue.put('ok')

def get_redis():
    connection_pool=redis.ConnectionPool(host='127.0.0.1',db=0)
    return redis.Redis(connection_pool=connection_pool)

def consumer():
    while True:
        task=rcon.rpop("queue")
        if not task:
            time.sleep(1)
            continue
        asyncio.run_coroutine_threadsafe(do_sleep(int(task),queue),new_loop)'''

'''if __name__ == '__main__':
    print(time.ctime())
    new_loop=asyncio.new_event_loop()
    #定义一个线程，运行一个事件循环对象，用于实时接收新任务
    loop_thread=Thread(target=start_loop,args=(new_loop,))
    loop_thread.setDaemon(True)
    loop_thread.start()
    #创建redis连接
    rcon=get_redis()
    queue=Queue()

    #子线程：用于消费队列消息，并实时往事件对象容器中添加新任务
    consumer_thread=Thread(target=consumer)
    consumer_thread.setDaemon(True)
    consumer_thread.start()

    while True:
        msg=queue.get()
        print("协程运行完..")
        print("当前时间：", time.ctime())'''

'''async def func1():
    print(1)
    await asyncio.sleep(2)
    print(2)

async def func2():
    print(3)
    await asyncio.sleep(3)
    print(4)

tasks=[
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))'''

import asyncio
async def func(x):
    print(x)
    await asyncio.sleep(x)
    print(x)
    return "返回值"

async def main():
    task_list=[
        asyncio.create_task(func(3),name='n1'),
        asyncio.create_task(func(1),name='n2')
    ]
    print('main结束')
    done,pending=await asyncio.wait(task_list,timeout=2)
    print(done)
    print(pending)

asyncio.run(main())
