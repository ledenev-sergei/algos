#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    profit = 0
    shares_bought = 0
    moneys_spent = 0

    max_price = max(prices)
    start_idx = 0

    while start_idx < len(prices):
        for i in range(start_idx, len(prices)):
            start_idx = i+1

            if prices[i] == max_price:
                profit += max_price * shares_bought - moneys_spent
                shares_bought = 0
                moneys_spent = 0

                if start_idx < len(prices):
                    max_price = max(prices[start_idx:])
                break

            shares_bought += 1
            moneys_spent += prices[i]

    return profit

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
