#!/usr/bin/env python3
'''Async generator'''
import asyncio
import random


async def async_generator():
    '''loops 10 times and yields a random number between 0 and 10'''
    for i in range(10):
        n = random.uniform(0, 10)
        yield n
        await asyncio.sleep(1)
