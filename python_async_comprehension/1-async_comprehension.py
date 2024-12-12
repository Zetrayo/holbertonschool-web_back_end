#!/usr/bin/env python3
"""
This module collects the numbers from async_generator using async comprehension.
"""

from Cheto import async_generator
from typing import List

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using an asynchronous comprehension
    and returns them as a list.
    """
    return [number async for number in async_generator()]
