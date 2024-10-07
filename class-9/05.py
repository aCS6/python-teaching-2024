def some(**kwargs):
    loggedin = kwargs.get("is_loggedin")
    username = kwargs.get("loggedin_user")

    if loggedin == False:
        return
    
    elif loggedin == True:
        print("You are loogedin")
        if username is not None:
            print(f'hello {username}')



some(is_loggedin=True)

some(is_loggedin=True, loggedin_user="nahid")

some(is_loggedin=False)
