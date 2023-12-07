#!/usr/bin/env python3
'''type-annotated function returns their sum as a float'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''takes in a list of float and returns their sum as a float'''
    return sum(input_list)
