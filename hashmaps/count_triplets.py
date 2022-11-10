#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    number_to_index_map = {}

    for i in range(0, len(arr)):
        current_number = arr[i]
        if current_number not in number_to_index_map:
            number_to_index_map[arr[i]] = [i]
        else:
            number_to_index_map[arr[i]].append(i)

    triplet_set = set()

    for first_num_idx in range(0, len(arr)):
        number = arr[first_num_idx]
        if number in number_to_index_map and number*r in number_to_index_map and number*r*r in number_to_index_map:
            for second_num_idx in number_to_index_map[number*r]:
                if second_num_idx > first_num_idx:
                    for third_num_idx in number_to_index_map[number*r*r]:
                        if third_num_idx > second_num_idx:
                            triplet_set.add((first_num_idx, second_num_idx, third_num_idx))

    return len(triplet_set)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
