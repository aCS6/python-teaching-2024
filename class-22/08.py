try:
    dc = {
        'name' : 'nahid'
    }
    number = 10 / 0
    
    print(dc['email'])
except ZeroDivisionError as e:
    print("Zero diye vag er jonno error")
except KeyError as e:
    print("Key paoa jay nai")
except:
    print("new error")