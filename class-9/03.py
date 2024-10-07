def sum_function(*args):
    sum = 0

    for number in args:
        sum = sum + number
    
    return sum


result = sum_function(1,2,3)
print(result)