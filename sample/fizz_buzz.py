#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#
from typing import Iterable


def fizzBuzz(n):
    for value in fizzBuzzSolution(n):
        print(value)

def fizzBuzzSolution(n) -> Iterable[str]:
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
            continue
        elif i % 3 == 0:
            yield "Fizz"
            continue
        elif i % 5 == 0:
            yield "Buzz"
            continue
        else:
            yield str(i)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
