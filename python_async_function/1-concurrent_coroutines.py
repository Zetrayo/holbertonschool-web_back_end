#!/usr/bin/env python3
"""
This module defines an asynchronous function `wait_n` that calls `wait_random`
multiple times to simulate waiting for random delays and returns these delays 
sorted in ascending order. It is useful for performing concurrent tasks with 
random delays and obtaining the delays in order.
"""


import asyncio
from typing import List
from importables import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously calls `wait_random` n times with a maximum delay and 
    returns a sorted list of the random delays.

    Parameters:
    n (int): The number of times to call `wait_random`.
    max_delay (int): The maximum delay time for each call.

    Returns:
    List[float]: A sorted list of the delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
