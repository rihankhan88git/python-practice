from fastapi import FastAPI
from students import students
app = FastAPI()
@app.get("/students")
def get_students():
    return students

@app.get("/students/{students_id}")
def get_student(students_id: int):
    student = students.get(students_id)
    return student

