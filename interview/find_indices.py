#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findIndices' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY query
#
def findIndices(n, query):
    range_intersection_count = [0] * n
    result = set()

    for l, r in query:
        for idx in range(l-1, r):
            range_intersection_count[idx] += 1

    if len(range_intersection_count) == 1:
        result.add(0)
        return result

    for i in range(0, len(range_intersection_count)):
        if range_intersection_count[i] == 1:
            result.add(i+1)

    if not result:
        result.add(-1)

    return sorted(list(result))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    query_rows = int(input().strip())
    query_columns = int(input().strip())

    query = []

    for _ in range(query_rows):
        query.append(list(map(int, input().rstrip().split())))

    result = findIndices(n, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
