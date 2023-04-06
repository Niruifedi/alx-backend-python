#!/usr/bin/env python3
"""
Measure Runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function calculate average time of the await coroutine
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = (time.perf_counter() - start_time)
    return total_time / n
