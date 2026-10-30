#!/usr/bin/env python3
"""
A module containing an asynchronous generator coroutine
that yields 10 random numbers with a 1-second delay each.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutines that loops 10 times, asynchronously waits 1 second,
    and yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
