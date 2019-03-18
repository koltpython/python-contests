#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    even_fibs = []
    f0 = 1
    f1 = 2
    while f1 <= n:
        if f1 % 2 ==0:
            even_fibs.append(f1)
        (f0, f1) = (f1, f0 + f1)
    print(sum(even_fibs))