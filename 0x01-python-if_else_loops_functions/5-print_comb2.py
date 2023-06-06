#!/usr/bin/python3
for y in range(0 , 100):
    print("{:02d}".format(y), end='')
    if y < 99:
        print(", ", end='')
