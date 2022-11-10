#!/bin/python3
import bisect
import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
import statistics
from collections import deque
from typing import List


def activityNotifications(expenditure, days):
    sliding_window = deque()
    sorted_sliding_window = []
    notify_count = 0

    for spent in expenditure:
        if len(sorted_sliding_window) == days and spent >= median(sorted_sliding_window)*2:
            notify_count += 1

        sliding_window.append(spent)
        bisect.insort_left(sorted_sliding_window, spent)

        if len(sliding_window) <= days:
            continue

        left = sliding_window.popleft()
        sorted_idx = bisect.bisect_left(sorted_sliding_window, left)
        del sorted_sliding_window[sorted_idx]

    return notify_count

    pass


def median(sorted_list: List[int]) -> float:
    if len(sorted_list) % 2 == 1:
        middle = math.floor(len(sorted_list) / 2)
        return sorted_list[middle]

    left = int(len(sorted_list)/2)-1

    return (sorted_list[left] + sorted_list[left + 1]) / 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
