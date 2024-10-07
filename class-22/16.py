import json

with open('myjson.json', 'r') as json_file:
    loaded = json.load(json_file)    

print(loaded)
print(type(loaded))