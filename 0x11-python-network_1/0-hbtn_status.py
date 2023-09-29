#!/usr/bin/python3
import urllib.request
url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print('Body response:')
    print('     - content: ',content)
    print('     - type: ',type(content))
    # response = urllib.request.urlopen(url)
    # data = response.read()
    decoded_data = content.decode("utf-8")
    print('     - utf8 content: ',decoded_data)
    # print(' - status code: ',response.getcode()) # 200
   