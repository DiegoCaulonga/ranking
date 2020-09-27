from src.app import app
from flask import request, Response
from src.database import db
from bson.json_util import dumps
from src.helpers.json_response import asJsonResponse


@app.route("/student/create/<student_name>")
def create_student(student_name):
    new_student = {"user": student_name}
    result = db.students.insert_one(new_student)
    return {"_id": str(result.inserted_id)}


@app.route('/student/all')
def list_students():
    res = db.students.distinct("user")
    return (dumps(res))


