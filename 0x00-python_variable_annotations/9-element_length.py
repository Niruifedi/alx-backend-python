#!/usr/bin/env python3
"""Sequence Annotation"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    computes length of a sequence
    """
    return [(i, len(i)) for i in lst]
