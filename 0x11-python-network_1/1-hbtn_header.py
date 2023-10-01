#!/usr/bin/python3
import urllib
import urllib.request
import sys
arg = sys.argv[1]
url = "https://alx-intranet.hbtn.io"
repons = urllib.request.urlopen(arg) 
print(repons.getheader("X-Request-Id"))

if __name__ == "__main__":
    pass
