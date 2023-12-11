#!/usr/bin/env python3
'''measuring elapsed runtime'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    '''function that takes 2 arguments and measures total execution time
    and returns total_time/n'''
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
