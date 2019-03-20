#!/bin/python3

import math
import os
import random
import re
import sys

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

# Complete the minimumNumber function below.


def minimumNumber(n, password):
    has_digit = False
    has_lc = False
    has_uc = False
    has_special = False
    for ch in password:
        if ch in numbers:
            has_digit = True
        elif ch in lower_case:
            has_lc = True
        elif ch in upper_case:
            has_uc = True
        elif ch in special_characters:
            has_special = True

    addition = 0
    if not has_digit:
        addition += 1
    if not has_lc:
        addition += 1
    if not has_uc:
        addition += 1
    if not has_special:
        addition += 1

    return max(addition, 6-n)

    # Return the minimum number of characters to make the password strong


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
