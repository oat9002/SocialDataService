# -*- coding: utf-8 -*-
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.types import *
import dateutil.parser as date
import json
from pymongo import MongoClient 


spark = SparkSession\
    .builder\
    .master("spark://stack-02:7077")\
    .config("spark.cores.max", 2)\
    .appName("SocialDataService")\
    .getOrCreate()

sc = spark.sparkContext


def getSocialDataByStartAndEnd(start, end):
    socialDataParquet = "hdfs://stack-02:9000/SocialDataRepository/SOCIALDATA.parquet"
    socialDataDF = spark.read.parquet(socialDataParquet)
    socialDataDF = socialDataDF.sort(socialDataDF.created_at.desc())
    socialData = socialDataDF.where(start >= socialDataDF.created_at).where(socialDataDF.created_at <= end).collect()
    sd_list = []
    for sd in socialData:
        sd_list.append(sd.asDict())
    return sd_list

def getTweetDataByStartAndEnd(start, end):
    client = MongoClient('mongodb://10.0.1.3:27017/')
    db = client['SocialData']
    tweet_collection = db.tweet
    tweets = tweet_collection.find({"created_at": {"$gte": date.parse(start), "$lte": date.parse(end)}})
    tw_list = []
    for tw in tweets:
        del tw['_id']
        tw_list.append(tw)
    return tw_list

def getAllSocialData():
    socialDataParquet = "hdfs://stack-02:9000/SocialDataRepository/SOCIALDATA.parquet"
    socialDataDF = spark.read.parquet(socialDataParquet)
    socialData = socialDataDF.collect()
    sd_list = []
    for sd in socialData:
        sd_list.append(sd.asDict())
    return sd_list

def getAllQuery():
    queryParquet = "hdfs://stack-02:9000/SocialDataRepository/QUERY.parquet"
    queryDF = spark.read.parquet(queryParquet)
    queries = queryDF.collect()
    q_list = []
    for q in queries:
        q_list.append(q.asDict())
    return q_list

def getPlaceById(place_id):
    # placeParquet = "../SocialDataRepository/PLACE.parquet"
    placeParquet = "hdfs://stack-02:9000/SocialDataRepository/PLACE.parquet"
    placeDF = spark.read.parquet(placeParquet)
    place = placeDF.where(placeDF.id == place_id).collect()
    place = place[0].asDict()
    return place

def get_predicted():
    client = MongoClient('mongodb://10.0.1.3:27017/')
    db = client['SocialData']
    predicted_collection = db.predicted
    predicted = predicted_collection.find().sort("_id", -1).limit(1)
    for p in predicted:
        predicted = p
    del predicted['_id']
    return predicted

def save_predicted(predicted):
    client = MongoClient('mongodb://10.0.1.3:27017/')
    db = client['SocialData']
    predicted_collection = db.predicted
    result = predicted_collection.insert_one({'id': predicted['id'], 'predicted': predicted['predicted']}).inserted_id
    return result