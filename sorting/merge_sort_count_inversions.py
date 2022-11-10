#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countInversions' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
from typing import List


def countInversions(arr):

    # Write your code here
    return mergeSort(arr)


def mergeSort(arr: List[int]) -> int:
    if len(arr) == 1:
        return 0

    mid_idx = len(arr)//2

    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]

    swaps_count = 0

    swaps_count += mergeSort(left_arr)
    swaps_count += mergeSort(right_arr)

    left_idx = right_idx = sorted_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            arr[sorted_idx] = left_arr[left_idx]
            left_idx += 1
        else:
            arr[sorted_idx] = right_arr[right_idx]
            right_idx += 1
            swaps_count += len(left_arr)-left_idx

        sorted_idx += 1

    while left_idx < len(left_arr):
        arr[sorted_idx] = left_arr[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right_arr):
        arr[sorted_idx] = right_arr[right_idx]
        right_idx += 1
        sorted_idx += 1

    return swaps_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
