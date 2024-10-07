username = 'demo'
print(username)

def some(username):
    # Function scope
    print(username)

print(username)

some(username='nahid')

print(username)