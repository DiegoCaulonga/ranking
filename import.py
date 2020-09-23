import requests
import json
import pymongo
import argparse

parser = argparse.ArgumentParser(description="Update MongoDB data")
parser.add_argument("-p","--page",type=int,help="page to import")
args = parser.parse_args()


def importapi(x):
    url = f"https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls?state=closed&page={x}&per_page=100"
    r = requests.get(url)
    pulls = json.loads(r.text)
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    your_db = client.pulls
    pull_collection = your_db.pull_requests
    result = pull_collection.insert_many(pulls)
    while len(pulls)>0:
        return result
        if len(pulls)==0:
            break

if __name__=="__main__":
    print(importapi(args.page))