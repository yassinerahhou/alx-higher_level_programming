<<<<<<< HEAD
#!/usr/bin/python3
import urllib.request
url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print('Body response:')
    print('\t- content: ',content)
    print('\t- type: ',type(content))
    # response = urllib.request.urlopen(url)
    # data = response.read()
    decoded_data = content.decode("utf-8")
    print('\t- utf8 content: ',decoded_data)
    # print(' - status code: ',response.getcode()) # 200
=======
#!/usr/bin/python3
import urllib.request
url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print('Body response:')
    print('\t- content: ',content)
    print('\t- type: ',type(content))
    # response = urllib.request.urlopen(url)
    # data = response.read()
    decoded_data = content.decode("utf-8")
    print('\t- utf8 content: ',decoded_data)
    # print(' - status code: ',response.getcode()) # 200
   
>>>>>>> 66174f566d2025a37ad5185dedf9720f9a54a2cd
