from config import DBURL
from pymongo import MongoClient

client = MongoClient("mongodb://localhost/pulls")
db = client.get_database()