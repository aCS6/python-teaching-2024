import json

student = {
    "id" : 1,
    "name" : "nahid",
    "department": "computer science"
}

student_json = json.dumps(student)
print(student_json)
print(type(student_json))