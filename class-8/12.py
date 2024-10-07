# Hello nahid , you can vote


def greet(username , age):
    """
        Key word argument
    """
    if age >=18:
        vote = "You can vote"
    else:
        vote = "You can not vote"


    print(f"Hello {username}, {vote}")

# positional argument
# greet("nahid" , 10)
# greet("amir" , 20)

greet(username="nahid" , age=10)
greet(age=20 , username="amir")