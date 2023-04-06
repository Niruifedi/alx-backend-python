#!/usr/bin/env python3
""" Basic asynchronous coroutine"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Async function take an integer as argument and return a float value
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
