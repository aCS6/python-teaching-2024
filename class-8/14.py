# Hello nahid
# Hello mahtab, you are from Franch

def greet(username , country=None):
    
    if country is None:
        print(f"Hello {username}")
    else:
        print(f"Hello {username}, you are from {country}")


greet(username="mahtab", country="Franch")
greet(username="nahid")

