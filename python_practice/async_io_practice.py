import asyncio
from asyncio import create_task, gather
from traceback import print_tb

class TerminateTaskGroup(Exception):
    """Exception raised to terminate a task group."""
#Basic function to run co_routine

async def co_routine(temp):

    await asyncio.sleep(temp)
    return f'returning after sleeping {temp} seconds'


# if __name__ == "__main__":
#     result = asyncio.run(co_routine(10))
#     print(result)
#
# #Co_routine with context manager
#
# if __name__ == "__main__":
#
#     with asyncio.Runner() as runner:
#         res = runner.run(co_routine(2))
#         res_1 = runner.run(co_routine(3))
#         res_2 = runner.run(co_routine(4))
#         print(res,res_1,res_1)

async def runner_task_group():
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(co_routine(3))
            task2 = tg.create_task(co_routine(4))
            task2 = tg.create_task(co_routine("jhvjyhf"))
        print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")
    except* TerminateTaskGroup as msg:
        print(msg)

async def runner_task_group_1():
    global task
    background_tasks = set()
    for i in range(10):
        task = asyncio.create_task(co_routine(10))

        # Add task to the set. This creates a strong reference.
        background_tasks.add(task)

        # To prevent keeping references to finished tasks forever,
        # make each task remove its own reference from the set after
        # completion:
        task.add_done_callback(background_tasks.discard)

    ressult = await task
    print(ressult)

async def runner_gater():

    gather_obj = asyncio.gather(
        co_routine(2),
        co_routine(3),
        co_routine(2),
    )
    result = await gather_obj
    print(result)

if __name__ == "__main__":

    asyncio.run(runner_gater())