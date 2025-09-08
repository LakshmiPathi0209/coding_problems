import asyncio

async def worker(name, delay):
    await asyncio.sleep(delay)
    if name == "Task B":
        raise ValueError("Oops in Task B")
    return f"{name} done"

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            t1 = tg.create_task(worker("Task A", 1))
            # t2 = tg.create_task(worker("Task B", 2))  # this raises
            t3 = tg.create_task(worker("Task C", 3))
        print(t1.result())
        print(t3.result())
    except* Exception as eg:  # Python 3.11+ "exception groups"
        print("Caught exception group:", eg)

asyncio.run(main())
