def some(a):
    return a**2

def another(a, b):
    return a+b

# print(some(50))
# print(another(10,20))

# Lambda Function

# def some(a):
#  return a**2

square = lambda a : a**2

print(square(10))
print(square(5))

# def another(a, b):
#     return a+b

two_sum = lambda a,b : a+b
print(two_sum(5,2))