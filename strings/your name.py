

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    """the idea is straightforward ,you split the string and then let
    capitalize() method to do the magic ,yet there was some problems oneof them is using s=s.split()
    thinking that default parameter for split
    is one space but that is not true it consider any number of spaces as one
    space. the other problem is using title() method ,this one violate the
    note in the problem explanation"""
    p=' '
    s=s.split(p)
    for i in range(len(s)):

        s[i]=s[i].capitalize()
    s=" ".join(s)
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
