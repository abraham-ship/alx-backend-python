#!/usr/bin/env python3
'''run time for parallel comprehensions'''
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    '''function to execute async_comprehension 4 times in parallel using
    asyncio.gather and return total runtime'''
    for _ in range(4):
        gather = await asyncio.gather(async_comprehension())
        total_time = [res[1] for res in gather]
        avg = sum(total_time)
        return avg
