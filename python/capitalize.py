#!/bin/python3

import math
import os
import random
import re
import sys


def solve(s):

    result = ""
    hasCapitalize = False

    for i in s:
        if i.isalpha() and not(hasCapitalize):
            hasCapitalize = True
            result += i.upper()
        else:
            if i == " ":
                hasCapitalize = False
            elif i.isdigit():
                hasCapitalize = True
            result += i
    return result


if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)
