#!/usr/bin/python3
"""yes"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """yes"""
    return lambda x: x * multiplier
