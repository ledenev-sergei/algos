#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def sherlockAndAnagrams(s):
    return hashMap(s)


def hashMap(s: str):
    anagrams_with_count = {}

    for left_idx in range(0, len(s)):
        for right_idx in range(left_idx+1, len(s)+1):
            anagram = ''.join(sorted(s[left_idx:right_idx]))
            anagrams_with_count[anagram] = anagrams_with_count.get(anagram, 0) + 1

    result = 0
    for current_count in anagrams_with_count.values():
        if current_count > 1:
            result += current_count*(current_count-1)/2

    return int(result)

def bruteForce(s: str):
    all_sorted_substrings = []

    for left_idx in range(0, len(s)):
        for right_idx in range(left_idx+1, len(s)+1):
            all_sorted_substrings.append(''.join(sorted(s[left_idx:right_idx])))

    anagrams_count = 0

    for i in range(0, len(all_sorted_substrings)):
        current_substring = all_sorted_substrings[i]
        for j in range(i+1, len(all_sorted_substrings)):
            if current_substring == all_sorted_substrings[j]:
                anagrams_count += 1
    # Write your code here

    return anagrams_count

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(f"Result: {result}")
