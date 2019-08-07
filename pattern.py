#!/usr/bin/python
from __future__ import print_function

def pattern(n):
    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")


x = 5 
pattern(x)
