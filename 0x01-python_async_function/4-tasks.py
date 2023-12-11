#!/usr/bin/env python3
'''executing multiple coroutines at the same time'''
import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    function that takes in two int arguments and returns a sorted list
    in ascending order
    '''
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        delays.append(delay)
    await asyncio.sleep(max(delays))
    return sorted(delays)
