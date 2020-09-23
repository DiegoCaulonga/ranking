from src.app import app
from flask import request, Response
from src.helpers.json_response import json_response
import re
from src.database import db

@app.route("student/create")
def createStudent():
    studentName = request.args.get("name")
    if not studentName:      
        return {"status": "error", "message": "Empty student name, please specify one"}, 400

   
    projection = {"name": 1, "category_code": 1,"description":1}
    searchRE = re.compile(f"{studentName}", re.IGNORECASE)
    foundStudent = db["student"].find_one({"name": searchRE}, projection)

    if not foundCompany:
        return {"status": "not found","message": f"No company found with name {companyNameQuery} in database"}, 404

    data = {"status": "OK", "searchName": studentName, "company": foundStudent}
    return json_response(data)