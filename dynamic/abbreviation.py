#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def abbreviation(a: str, b: str):
    dp = []

    for i in range(len(a)+1):
        dp.append([])
        for j in range(len(b)+1):
            dp[i].append(False)

    dp[0][0] = True

    for b_idx in range(len(b)):
        for a_idx in range(len(a)):
            a_char = a[a_idx]
            b_char = b[b_idx]

            if dp[a_idx][b_idx]:
                if b_idx < len(b) and a_char.upper() == b_char:
                    dp[a_idx+1][b_idx+1] = True

                if not a_char.isupper():
                    dp[a_idx + 1][b_idx] = True

    if dp[len(a)][len(b)]:
        return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
