#!/usr/bin/env python3
"""
This is so it's easier to import things
"""

import asyncio
import random
from typing import AsyncGenerator, List


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates a random number between 0 and 10, 10 times,
    with a 1-second delay between each.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an asynchronous comprehension
    and returns them as a list.
    """
    return [number async for number in async_generator()]
