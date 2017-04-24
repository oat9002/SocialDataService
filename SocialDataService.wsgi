import sys
import os
sys.path.insert(0, '/usr/local/nodejs/SocialDataService')
sys.path.append('/usr/local/spark/python')
os.environ['SPARK_HOME'] = '/usr/local/spark/'

from index import app as application