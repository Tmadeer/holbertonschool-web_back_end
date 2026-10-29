#!/usr/bin/env python3
"""Module that spawns several tasks concurrently using task_wait_random."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return the delays in order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays
