#!/usr/bin/env python3
"""
This module defines a function to create a multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a multiplier (float) and returns a function that multiplies 
    its input by the multiplier.

    Args:
        multiplier (float): The value by which the input will be multiplied.

    Returns:
        Callable[[float], float]: A function that multiplies its input by the multiplier.
    """
    return lambda x: x * multiplier
