import asyncio
import time
from concurrent.futures import ProcessPoolExecutor

def cpu_bound_operation(x):
    time.sleep(x) # This is some operation that is CPU-bound
    print('The end')

async def task(x):
	await loop.run_in_executor(p, cpu_bound_operation, x)

async def main():
    # Run cpu_bound_operation in the ProcessPoolExecutor
    # This will make your coroutine block, but won't block
    # the event loop; other coroutines can run in meantime.
    t1 = asyncio.create_task(task(2))
    t2 = asyncio.create_task(task(3))
    await t1
    await t2

loop = asyncio.get_event_loop()
p = ProcessPoolExecutor(2) # Create a ProcessPool with 2 processes
loop.run_until_complete(main())
