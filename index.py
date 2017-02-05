# -*- coding: utf-8 -*-
from services import SocialDataService
from flask import Flask, request
import json


app = Flask(__name__)

@app.route("/socialdata/data", methods=['GET'])
def getSocialData():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getSocialData(start, end)
    return data

@app.route("/query", methods=['GET'])
def getAllQuery():
    data = SocialDataService.getAllQuery()
    return data

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005, threaded=True)
