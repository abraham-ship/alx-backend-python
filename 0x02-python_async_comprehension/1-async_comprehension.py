#!/usr/bin/env python3
'''Async comprehension'''
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''this collects 10 random numbers using async comprehesion
    over async_generator and returns 10 random numbers'''
    res = [i async for i in async_generator()]
    return res
