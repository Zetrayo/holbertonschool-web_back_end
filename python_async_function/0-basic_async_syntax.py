#!/usr/bin/env python3
"""
This module provides an asynchronous function that simulates waiting for
a random amount of time between 0 and a specified maximum delay.
It is useful for scenarios where a random delay is needed, such as 
simulating unpredictable network latency.
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and max_delay (inclusive),
    and returns the delay value.

    Parameters:
    max_delay (int): The maximum delay time (default is 10).

    Returns:
    float: The random delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
