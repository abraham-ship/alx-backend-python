#!/usr/bin/env python3
'''type-annotated function that returns a function that multiplies a
float by multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
