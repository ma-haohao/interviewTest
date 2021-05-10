import asyncio
#协程的并发
async def do_some_work(x):
    print('Waiting:',x)
    await asyncio.sleep(x)
    return 'Done after {} s.'.format(x)

#生成协程对象
coroutine1=do_some_work(1)
coroutine2=do_some_work(2)
coroutine3=do_some_work(4)

#将协程转换成task，并组成list
tasks=[
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
]

#将协程注册到事件循环中去
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

'''loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))'''
for task in tasks:
    print('Task ret:',task.result())
