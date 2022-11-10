#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
from collections import defaultdict


def freqQuery(queries):
    value_to_freq = defaultdict(int)
    freq_count = defaultdict(int)
    result = []

    for query, value in queries:
        if query == 1:
            if freq_count[value_to_freq[value]]:
                freq_count[value_to_freq[value]] -= 1
            value_to_freq[value] += 1
            freq_count[value_to_freq[value]] += 1
        elif query == 2:
            if value_to_freq[value]:
                freq_count[value_to_freq[value]] -= 1
                value_to_freq[value] -= 1
                freq_count[value_to_freq[value]] += 1
        else:
            # operation 3
            if value in freq_count and freq_count[value]:
                result.append(1)
            else:
                result.append(0)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
