#!/usr/bin/python3
"""yes"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """yes"""
    return [(i, len(i)) for i in lst]
