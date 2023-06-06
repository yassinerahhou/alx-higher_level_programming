#!/usr/bin/python3
for y in range(97, 123):
    if chr(y) not in ['q','e']:
        print("{}".format(chr(y)), end='')
