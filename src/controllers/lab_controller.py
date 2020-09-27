from src.app import app
from flask import request, Response
from src.database import db
#from src.cleaning import result1

@app.route("/lab/create/<name>")
def create_lab(name):
    new_lab = {'Lab': name}
    result = db.labs.insert_one(new_lab)
    return {'_id': str(result.inserted_id)}



