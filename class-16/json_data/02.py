import json

student = {
    "id" : 1,
    "name" : "nahid",
    "department": "computer science"
}

# dictionary to json
student_json = json.dumps(student)
# print(student_json)


# json to dictionary
student_dict = json.loads(student_json)
print(student_dict)
print(type(student_dict))


# self study : dump , load