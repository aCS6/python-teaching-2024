# Multiple return
person = [
    {"name" : "nahid", "email" : "abc@gmail.com"},
    {"name" : "anil", "email" : "def@gmail.com"},
]

def get_person_info(person_id):
    print(f"You want the {person_id}'s information")
    
    person_id = person_id - 1

    name = person[person_id]["name"]
    email = person[person_id]["email"]

    return name, email # ->  (name , email)



# x = get_person_info(1)

# print(x[0])
# print(x[1])

username, user_age = get_person_info(2)

print(username)
print(user_age)

# multiple assign
# a , b = [10,20]