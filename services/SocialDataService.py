# -*- coding: utf-8 -*-
from pyspark import SparkContext
from pyspark.sql import *
from pyspark.sql.types import *
import dateutil.parser as date
import json


spark = SparkSession\
    .builder\
    .appName("SocialDataService")\
    .getOrCreate()

sc = spark.sparkContext


def getSocialData(start, end):
    socialDataParquet = "../SocialDataRepository/SOCIALDATA.parquet"
    socialDataDF = spark.read.parquet(socialDataParquet)
    socialDataDF = socialDataDF.sort(socialDataDF.created_at.desc())
    socialData = socialDataDF.where(start >= socialDataDF.created_at).where(socialDataDF.created_at <= end).collect()
    sd_list = []
    for sd in socialData:
        sd_list.append(sd.asDict())
    return sd_list


def getAllQuery():
    queryParquet = "../SocialDataRepository/QUERY.parquet"
    queryDF = spark.read.parquet(queryParquet)
    queries = queryDF.collect()
    q_list = []
    for q in queries:
        q_list.append(q.asDict())
    return q_list
