#!/usr/bin/python3
"""yes"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """yes"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
