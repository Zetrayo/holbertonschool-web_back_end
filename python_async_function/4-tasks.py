#!/usr/bin/python3
"""yes"""


import asyncio
from importables import task_wait_random


async def task_wait_n(n: int, max_delay: int):
    """yes"""
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return delays
