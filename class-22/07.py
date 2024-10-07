try:
    dc = {
        'name' : 'nahid'
    }
    number = 10 / 0
    
    print(dc['email'])
except Exception as e:
    print("Error ", e)