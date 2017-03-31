# -*- coding: utf-8 -*-
from services import SocialDataService
from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

@app.route("/socialdata/date", methods=['GET'])
def getSocialDataByStartAndEnd():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getSocialDataByStartAndEnd(start, end)
    socials = {}
    socials['socials'] = data
    return jsonify(socials)

@app.route("/socialdata", methods=['GET'])
def getAllSocialData():
    data = SocialDataService.getAllSocialData()
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

@app.route("/predicted", methods=['GET'])
def get_predicted():
    predicted = {}
    predicted['predicted'] = SocialDataService.get_predicted();
    return jsonify(predicted) 

@app.route("/predicted/save", methods=['POST'])
def save_predicted():
    predicted = json.loads(request.get_data())
    result = SocialDataService.save_predicted(predicted)
    if result == None:
        return  ('', 500)
    else:
        return ('', 204)

@app.route("/tweet/date", methods=['GET'])
def getTweetDataByStartAndEnd():
    start = request.args.get('start')
    end = request.args.get('end')
    data = SocialDataService.getTweetDataByStartAndEnd(start, end)
    tweet = {}
    tweet['tweets'] = data
    return jsonify(tweet)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5005, threaded=True)
