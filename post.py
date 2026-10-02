from fastapi import FastAPI
from courses import courses
app = FastAPI()

@app.get("/courses")
def get_courses():
    return courses
#
# @app.get("/courses/{course_id}")
# def get_course(course_id: str):
#     course = courses.get(course_id)
#     return course


