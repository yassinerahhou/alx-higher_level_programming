#!/usr/bin/python3

import sys
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as repons:
        body = repons.info()
        d = 'X-Request-Id'
        if d in body:
            st = body[d]
            print(st)