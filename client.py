# -*- coding: utf-8 -*-
import requests
import json

url = "http://invisiondev.iptime.org:33001/"
files = {'file': ("test.png", open('test.png', 'rb'))}
res = requests.post(url, files=files)
if res.status_code == 200:
    with open('test.obj', 'wb') as file:
        file.write(res.content)
    print("Success.")