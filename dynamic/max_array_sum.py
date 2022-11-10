#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

"""
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that 
subset. It is possible that the maximum sum is , the case when all elements are negative.
"""
# Complete the maxSubsetSum function below.
def maxSubsetSum(arr: List[int]):
    """
    there are two options for each element in arr, include to subset or not.
    Let's define list containing the best possible answer till index i
    """
    best_answer_till_index = [0] * len(arr)

    best_answer_till_index[0] = max(0, arr[0])
    best_answer_till_index[1] = (max(best_answer_till_index[0], arr[1]))

    for i in range(2, len(arr)):
        best_answer_till_index[i] = max(
            best_answer_till_index[i-2],
            max(best_answer_till_index[i-1], best_answer_till_index[i-2] + arr[i])
        )

    return max(best_answer_till_index[len(arr)-1], best_answer_till_index[len(arr)-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
