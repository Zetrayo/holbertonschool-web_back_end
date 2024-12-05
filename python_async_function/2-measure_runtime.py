#!/usr/bin/env python3
"""
This module defines a function `measure_time` that measures the total execution 
time of calling the `wait_n` function multiple times and returns the average 
time per call. It uses the `time` module to calculate the elapsed time and 
`asyncio` to execute the asynchronous `wait_n` function.
"""


import asyncio
import time
from importables import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for `wait_n` and returns the average 
    time per call.

    Parameters:
    n (int): The number of times to call `wait_n`.
    max_delay (int): The maximum delay for each call to `wait_random` inside `wait_n`.

    Returns:
    float: The average time per call of `wait_n`.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
