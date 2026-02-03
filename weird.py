#!/bin/python3

import math
import os
import random
import re
import sys

def weird_number_check(n):
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':
    n = int(input().strip())
    weird_number_check(n)