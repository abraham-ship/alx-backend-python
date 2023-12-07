#!/usr/bin/env python3
'''type-annotated function returns their sum as a float'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''function takes in a list of float and integer and
    returns their sum as float'''
    return sum(mxd_lst)
