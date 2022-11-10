#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
The absolute difference is the positive difference between two values a and b , is written |a-b| or |b-a| 
and they are equal. If a = 3 and b = 2, |3-2| = |2-3| = 1 . Given an array of integers, find the minimum absolute 
difference between any two elements in the array.
"""

def minimumAbsoluteDifference(arr):
    arr.sort()

    current_min = sys.maxsize

    for i in range(len(arr)-1):
        current_value = arr[i]
        next_value = arr[i+1]

        if abs(current_value-next_value) < current_min:
            current_min = abs(current_value-next_value)
    return current_min
# Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
