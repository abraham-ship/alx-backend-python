#!/usr/bin/env python3
'''update function parameters with their appropriate types'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''anottating parameters with appropriate types'''
    return [(i, len(i)) for i in lst]
