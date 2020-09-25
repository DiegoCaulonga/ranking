from src.app import app
from flask import request, Response
from src.database import db
from bson.json_util import dumps
from src.cleaning import result1 

@app.route("/student/create/<student_name>")
def create_student(student_name):
    new_student = {"user": student_name}
    result = db.students.insert_one(new_student)
    return {"_id": str(result.inserted_id)}



@app.route("/student/labs/<x>")
def resultado(x):
    student_labs = {"student": x,
                    "labs": result1[result1["student"]==x]["lab"]}
    result = db.student.insert_many(student_labs)
    return {"id": str(result.inserted_id)}