# -*- coding: utf-8 -*-
from repository import SocialDataRepository
from flask import Flask, request
import json


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/read", methods=['GET'])
def readTweet():
    TwitterRepository.readTweet()
    return ('', 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
