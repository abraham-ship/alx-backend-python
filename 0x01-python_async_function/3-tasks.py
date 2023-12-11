#!/usr/bin/env python3
'''function to return asyncio task'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[str]:
    '''function that takes an int and returns an asyncio task'''
    task = asyncio.create_task(wait_random(max_delay))
    return task
