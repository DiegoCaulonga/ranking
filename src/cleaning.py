import requests
import json
import os
import regex as re
from dotenv import load_dotenv
import pandas as pd
import regex
from controllers.functions import lab,meme


def getpulls(num):
    res=requests.get(f"https://api.github.com/repos/ironhack-datalabs/datamad0820/pulls/{num}")
    if res.status_code == 404:
        return 'exit'
    
    data = res.json()
    return {
        "id":data["number"],
        "user":data["user"]["login"],
        "lab": lab(data["title"]),   
        "meme": meme(data["body"])}

data = []
for i in range(1000):
    if getpulls(i)=="exit":
        pass
    else:
        data.append(getpulls(i))

jsn = pd.DataFrame(data)
jsn.to_json("output/clean.json",orient="records")
