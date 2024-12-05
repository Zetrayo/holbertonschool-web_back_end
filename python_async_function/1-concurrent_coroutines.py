#!/usr/bin/python3
"""yes"""


import asyncio
from typing import List
from importables import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """yes"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
