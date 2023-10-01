#!/usr/bin/python3
#Python script that takes in a URL, sends a request to t
import urllib
import urllib.request
import sys
if __name__ == "__main__":
    
    arg = sys.argv[1]
    
    with urllib.request.urlopen(arg) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
