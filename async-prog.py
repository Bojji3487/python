
import asyncio,time


async def my_coro():
    print('Pausing coroutine')
    await asyncio.sleep(5)
    print('Resumed coroutine')

async def mid():
    print('heyyyyy')

start=int(time.time())
print('program started')
asyncio.run(my_coro())
print(f'mid time= {start-int(time.time())}')
asyncio.run(mid())
print(f'end time= {start-int(time.time())}')
