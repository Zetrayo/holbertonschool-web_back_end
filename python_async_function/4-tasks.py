#!/usr/bin/env python3
"""
This module defines an asynchronous function `task_wait_n` that calls 
`task_wait_random` n times with a maximum delay and returns the delays as a list.
"""


import asyncio
from typing import List
from importables import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously calls `task_wait_random` n times with a maximum delay and 
    returns a list of the random delays.

    Parameters:
    n (int): The number of times to call `task_wait_random`.
    max_delay (int): The maximum delay time for each call.

    Returns:
    List[float]: A list of the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return delays
