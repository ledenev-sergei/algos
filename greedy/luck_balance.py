#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#
from typing import List, Tuple

"""
Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. 
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. Each contest is 
described by two integers, L[i] and T[i]:

* L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i] ; 
if she loses it, her luck balance will increase by L[i].

* T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0 
if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all 
the preliminary contests? This value may be negative.
"""

def luckBalance(k: int, contests: List[Tuple[int, int]]):
    important_contests_luck = []
    total_luck = 0

    for luck, importance in contests:
        if importance == 1:
            important_contests_luck.append(luck)
        else:
            total_luck += luck

    important_contests_luck.sort(reverse=True)

    total_luck += sum(important_contests_luck[0:k]) - sum(important_contests_luck[k:])

    return total_luck


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
