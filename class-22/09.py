def vote(age):
    if age < 18:
        raise ValueError("Your age is not greater than 18")
    
    return True


try:
    vote(10)
except Exception as e:
    print(e)

vote(20)


try:
    vote(15)
except ValueError as e:
    print(e)