#!/usr/bin/env python3
'''run time for parallel comprehensions'''
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''function to execute async_comprehension 4 times in parallel using
    asyncio.gather and return total runtime'''
    start = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end = asyncio.get_event_loop().time()
    total = end - start
    return total
