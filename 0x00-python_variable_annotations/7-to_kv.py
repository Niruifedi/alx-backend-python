#!/usr/bin/env python3
"""string, int/float annotation"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function takes k: str, v:union of int or float
    and returns a tuple of str and float.
    """
    sqr = v ** 2
    return (k, sqr)
