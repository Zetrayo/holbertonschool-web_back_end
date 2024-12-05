#!/usr/bin/python3
"""yes"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """yes"""
    return (k, float(v ** 2))
