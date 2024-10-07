# Hello nahid , you can vote


def greet(username , age):
    """
        Multiple parameter example
    """
    if age >=18:
        vote = "You can vote"
    else:
        vote = "You can not vote"


    print(f"Hello {username}, {vote}")

greet("nahid" , 10)
greet("amir" , 20)