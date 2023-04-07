#!/usr/bin/env python3
"""
Runtime for coroutines
"""
import asyncio
import time
from typing import Generator

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    function counts the amount of time used in running
    the 4 coroutines in parallel
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
