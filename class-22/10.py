import json

person = {
    "name" : "nahid",
    "email" : "abc@yopmail.com"
}

# Dictionary to JSON
person_json = json.dumps(person)
print(type(person_json))


# JSON to Dictionary
person2 = json.loads(person_json)
print(person2)
print(type(person2))