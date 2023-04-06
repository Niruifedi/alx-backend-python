#!/usr/bin/env python3
"""
Tasks
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function creates a tasks from a coroutine
    """
    tasks = asyncio.create_task(wait_random(max_delay))
    return tasks
