#!/usr/bin/env python3
"""callable Annotations"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    function takes a float: multiplier
    return a callable function that returns float
    """
    return lambda x: x * multiplier
