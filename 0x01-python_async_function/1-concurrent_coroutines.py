#!/usr/bin/env python3
'''executing multiple coroutines at the same time'''
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function that takes in two int arguments and returns a sorted list
    in ascending order
    '''
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay=max_delay)
        delays.append(delay)
    await asyncio.sleep(max(delays))
    return sorted(delays)
