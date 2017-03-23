# -*- coding: utf-8 -*-
from services import SocialDataService
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/socialdata/data", methods=['GET'])
def getSocialData():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getSocialData(start, end)
    socials = {}
    socials['socials'] = data
    return jsonify(socials)

@app.route("/query", methods=['GET'])
def getAllQuery():
    data = SocialDataService.getAllQuery()
    queries = {}
    queries['queries'] = data
    return jsonify(queries)

@app.route("/place", methods=['GET'])
def getPlaceById():
    place_id = request.args.get('place_id')
    place = {}
    place['place'] = SocialDataService.getPlaceById(place_id)
    return jsonify(place)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005, threaded=True)
