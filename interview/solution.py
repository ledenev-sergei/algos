#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxProfit' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY pnl
#  2. INTEGER k
#
from collections import deque
from functools import lru_cache
from typing import List


def getMaxProfit(pnl, k):
    max_pnl = pnl[0]
    cur_sum_deque = deque()
    cur_sum_deque_sum = 0

    for value in pnl:
        if len(cur_sum_deque) == k:
            left = cur_sum_deque.popleft()
            cur_sum_deque_sum -= left

        if cur_sum_deque_sum < 0:
            cur_sum_deque = deque()
            cur_sum_deque_sum = 0

        cur_sum_deque.append(value)
        cur_sum_deque_sum += value
        max_pnl = max(max_pnl, cur_sum_deque_sum)

    while cur_sum_deque:
        left = cur_sum_deque.popleft()
        cur_sum_deque_sum -= left
        max_pnl = max(max_pnl, cur_sum_deque_sum)

    return max_pnl


# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pnl_count = int(input().strip())

    pnl = []

    for _ in range(pnl_count):
        pnl_item = int(input().strip())
        pnl.append(pnl_item)

    k = int(input().strip())

    result = getMaxProfit(pnl, k)

    fptr.write(str(result) + '\n')

    fptr.close()
