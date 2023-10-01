#!/usr/bin/python3
#Python script that takes in a URL, sends a request to t
import urllib
import urllib.request
import sys
if __name__ == "__main__":
    
    arg = sys.argv[1]
    url = "https://alx-intranet.hbtn.io"
    with urllib.request.urlopen(arg) as repons :
    # repons = urllib.request.urlopen(arg) 

        print(repons.getheader("X-Request-Id"))
