#!/usr/bin/env python3
"""Mixed List Annotation"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function collects a list mixed with int and float,
    using Union to combine both
    returns the sum in float
    """
    return sum(mxd_lst)
