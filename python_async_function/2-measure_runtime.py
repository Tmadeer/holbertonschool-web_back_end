#!/usr/bin/env python3
"""Module that measures the average runtime of the wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average time per coroutine taken by wait_n(n, max_delay)."""
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.time()
    total_time: float = end - start
    return total_time / n
