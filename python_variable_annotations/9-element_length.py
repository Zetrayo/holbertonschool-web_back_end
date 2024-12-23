#!/usr/bin/env python3
"""
This module defines a function that returns the length of each element in a list of sequences.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This function takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence and its corresponding length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequences (e.g., strings, lists).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
