#!/usr/bin/python3

def printAlphaRev():
    for c in range(ord('z'), ord('a') - 1, -1):
        print("{}".format(chr(c) if c % 2 == 0 else chr(c - 32)), end="")


printAlphaRev()
