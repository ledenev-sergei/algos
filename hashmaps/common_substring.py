#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoStrings' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def twoStrings(s1, s2):
    s1_substrings = set()

    for left_ptr in range(0, len(s1)-1):
        for right_ptr in range(left_ptr+1, len(s1)):
            s1_substrings.add(s1[left_ptr:right_ptr])

    for left_ptr in range(0, len(s2)-1):
        for right_ptr in range(left_ptr+1, len(s2)):
            if s2[left_ptr:right_ptr] in s1_substrings:
                return "YES"

    return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open("../output.txt", 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
