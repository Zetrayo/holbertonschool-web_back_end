#!/usr/bin/env python3
"""
This module  measures execution time for multiple parallel comprehensions.
"""

import asyncio
from Cheto import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime to execute async_comprehension four times in parallel
    using asyncio.gather and returns the total runtime in seconds.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
