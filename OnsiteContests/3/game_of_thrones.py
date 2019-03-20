#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    
    # # Idea 1: Without dict or set
    # # This solution fails on big input since it is slow
    # # for loop iterates over all characters, and count
    # # function iterates over all characters each time
    # odd_character = None
    # for char in s:
    #     count = s.count(char)
    #     if count % 2 == 1:
    #         if odd_character != None and char != odd_character:
    #             return 'NO'
    #         odd_character = char
    # return 'YES'

    # # Idea 2: Count character occurrences with dict
    # char_count_dictionary = {}
    
    # for char in s:
    #     if char in char_count_dictionary:
    #         char_count_dictionary[char] += 1
    #     else:
    #         char_count_dictionary[char] = 1
    
    # odd_counter = 0
    # for key, value in char_count_dictionary.items():
    #     if value % 2 == 1:
    #         odd_counter += 1
    
    # if odd_counter < 2:
    #     return 'YES'
    # else:
    #     return 'NO'

    # Idea 3: Find odd characters with set
    chars = set()
    for char in s:
        if char in chars:
            chars.remove(char)
        else:
            chars.add(char)
    if len(chars) < 2:
        return 'YES'
    else:
        return 'NO'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
