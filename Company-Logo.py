import math
import os
import random
import re
import sys
import collections


if __name__ == '__main__':
    s = sorted(input())
    unique = []
    for char in s[::]:
        if char not in unique:
            unique.append(char)
    if(len(unique)) >= 3:

        x = collections.Counter(s)
        sort_by_value = dict(
            sorted(x.items(), key=lambda item: item[1], reverse=True)[:3])
        # print(sort_by_value)

        for key, value in sort_by_value.items():

            print(key, value)
