#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    # If arr is MxN, i.e, len(arr) == M, len(arr[0]) == N
    # We have (M-2)*(N-2) hourglasses
    m = len(arr)
    n = len(arr[0])
    # Start with minus infinity
    max_hourglass = -float('inf')
    for i in range(1, m-1):
        for j in range(1, n-1):
            # Add the center
            hourglass_sum = arr[i][j]
            # Add the upper three
            hourglass_sum += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
            # Add the lower three
            hourglass_sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]

            if hourglass_sum > max_hourglass:
                max_hourglass = hourglass_sum

    return max_hourglass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
