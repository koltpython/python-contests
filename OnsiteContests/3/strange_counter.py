#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.


def strangeCounter(t):
    bound = 3
    while t > bound:
        t -= bound
        bound *= 2
    return bound - t + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
