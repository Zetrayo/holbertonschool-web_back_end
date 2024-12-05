#!/usr/bin/env python3
"""
This module contains a function to calculate the sum of a mixed list of integers and floats.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function takes a list of integers and floats as input and returns the sum of the elements
    as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and/or floats.

    Returns:
        float: The sum of the elements in the input list.
    """
    return float(sum(mxd_lst))
