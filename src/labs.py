from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
import re
from src.database import db

@app.route("lab/create")
def createLab():
    labName = request.args.get("lab")
    if not labName:      
        return {"status": "error", "message": "Empty lab name, please specify one"}, 400

   
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{labName}", re.IGNORECASE)
    foundLab = db["student"].find_one({"name": searchRE}, projection)

    if not foundCompany:
        return {"status": "not found","message": f"No company found with name {labName} in database"}, 404

    data = {"status": "OK", "searchName": labName, "company": foundLab}
    return json_response(data)