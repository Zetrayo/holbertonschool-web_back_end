#!/usr/bin/env python3
"""
This module defines a function to create a tuple with a string and the square of a number.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and an integer or float, and returns a tuple where the first 
    element is the string and the second element is the square of the number (as a float).

    Args:
        k (str): The string to be included in the tuple.
        v (Union[int, float]): The number to be squared and converted to a float.

    Returns:
        Tuple[str, float]: A tuple containing the string and the square of the number as a float.
    """
    return (k, float(v ** 2))
