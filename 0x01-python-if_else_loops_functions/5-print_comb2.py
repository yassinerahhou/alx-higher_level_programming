#!/usr/bin/python3
for y in range(100):
    if y != 99:
        print("{:02d}, ".format(y), end='')
    else:
        print("{:02d}".format(y))
