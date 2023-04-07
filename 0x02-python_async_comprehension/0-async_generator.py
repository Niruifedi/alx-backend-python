#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Function yields random float values at every iteration
    """
    for i in range(10):
        await asyncio.sleep(1)
        s = yield random.uniform(0, 10)
