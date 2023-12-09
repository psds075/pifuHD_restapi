# -*- coding: utf-8 -*-
import requests
import json
import cv2
import base64

image = cv2.imread('test.png')
data = base64.b64encode(cv2.imencode('.jpg', image)[1]).decode()
mydata = {'data' : data}

# send http request with image and receive response
response = requests.post('http://invisiondev.iptime.org:33001/', json=mydata)
data = response.content
with open("test.obj", 'wb') as s:
    s.write(data)

#result = json.loads(response.text)['message']
#print(result)
