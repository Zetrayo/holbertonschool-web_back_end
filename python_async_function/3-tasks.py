#!/usr/bin/python3
import asyncio
from importables import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
