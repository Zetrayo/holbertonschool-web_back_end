#!/usr/bin/env python3
"""
This module defines an asynchronous function `task_wait_n` that creates multiple 
tasks using `task_wait_random`, waits for all of them to complete, and returns 
the delays for each task.
"""


import asyncio
from importables import task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """
    Creates and executes multiple `task_wait_random` tasks concurrently.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay value to pass to `task_wait_random`.

    Returns:
    List[float]: A list of delays for each completed task.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
