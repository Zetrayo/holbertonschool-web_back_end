#!/usr/bin/python3
"""yes"""


import asyncio
import random
from typing import List
import time


async def wait_random(max_delay: int = 10) -> float:
    """yes"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

async def wait_n(n: int, max_delay: int) -> List[float]:
    """yes"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)

def measure_time(n: int, max_delay: int) -> float:
    """yes"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

def task_wait_random(max_delay: int) -> asyncio.Task:
    """yes"""
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int):
    """yes"""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return delays
