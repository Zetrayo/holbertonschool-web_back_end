#!/usr/bin/env python3
"""
This module defines a function `task_wait_random` that creates and returns an 
asynchronous task that runs the `wait_random` function. The function is designed 
to be used in concurrent programming with asyncio.
"""


import asyncio
from importables import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio Task that runs the `wait_random` coroutine.

    Parameters:
    max_delay (int): The maximum delay value to pass to `wait_random`.

    Returns:
    asyncio.Task: The task running the `wait_random` coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
