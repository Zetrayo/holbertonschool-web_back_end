#!/usr/bin/env python3
"""
This module contains asynchronous functions for generating random delays 
and executing them concurrently, as well as measuring the total execution time 
and creating tasks for the delays.
"""


import asyncio
import random
from typing import List
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    Generates a random float delay between 0 and max_delay, waits for that delay, 
    and returns the delay.

    Parameters:
    max_delay (int): The maximum delay value.

    Returns:
    float: A randomly generated delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates and waits for multiple `wait_random` tasks concurrently. Returns 
    the delays for each completed task in ascending order.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay value for each task.

    Returns:
    List[float]: A sorted list of delays for each completed task.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for executing `wait_n(n, max_delay)`, 
    and returns the average execution time per task.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay value for each task.

    Returns:
    float: The average time taken per task.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that will execute the `wait_random` 
    coroutine with a given max_delay.

    Parameters:
    max_delay (int): The maximum delay value to pass to `wait_random`.

    Returns:
    asyncio.Task: A task representing the `wait_random` coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int):
    """
    Creates and executes multiple `task_wait_random` tasks concurrently. 
    Returns the delays for each completed task.

    Parameters:
    n (int): The number of tasks to create.
    max_delay (int): The maximum delay value to pass to `task_wait_random`.

    Returns:
    List[float]: A list of delays for each completed task.
    """
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return delays
