from collections.abc import Coroutine
import asyncio
import time
async def hello(name):
    await asyncio.sleep(2)
    print('Hello',name)

#定义协程对象
async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒'.format(x)

coroutine=_sleep(2)

#定义时间循环对象的容器
loop=asyncio.get_event_loop()

#将写成转换称为task对象
task=asyncio.ensure_future(coroutine)

#利用回调函数获取协程的返回值
def callback(future):
    print('这里是回调函数，获取的返回结果为：',future.result())
task.add_done_callback(callback)
#将task任务扔进事件循环对象中并触发
loop.run_until_complete(task)
