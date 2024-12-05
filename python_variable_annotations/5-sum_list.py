#!/usr/bin/env python3
"""
This module contains a function to calculate the sum of a list of floats.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats as input and returns the sum of the elements
    as a float.

    Args:
        input_list (List[float]): A list containing float numbers.

    Returns:
        float: The sum of the elements in the input list.
    """
    return float(sum(input_list))
