# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:58:48 2020
@author: psds0
"""

from flask import Flask, request, Response, send_from_directory
import jsonpickle
import json
import numpy as np
import cv2
import base64
import prediction
import sys


# Initialize the Flask application
app = Flask(__name__)

# route http posts to this method
@app.route('/', methods=['POST'])
def api():
    r = request
    data = base64.b64decode(r.json['data'])
    data = np.frombuffer(data, dtype = np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imwrite("input/input.png", img)
    prediction.prediction()
    response = {'message': "complete"}
    response_pickled = jsonpickle.encode(response)
    #return Response(response=response_pickled, status=200, mimetype="application/json")
    return send_from_directory("output/pifuhd_final/recon", "result_input_256.obj")

import sys

port = 33001
debug = True
if(len(sys.argv) > 1):
    port = sys.argv[1]
if(len(sys.argv) > 2):
    if(sys.argv[2] == "False"):
        import logging
        debug = False 
        logging.basicConfig(filename='server.log',level=logging.DEBUG)


# start flask app
app.run(host="0.0.0.0", port=port, debug = debug)





