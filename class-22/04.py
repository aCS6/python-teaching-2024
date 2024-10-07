def calculate(number1, number2):
    try:
        return number1 / number2
    except:
        return 'Error'

print("Line 1")
print("Line 2")

print(calculate(10 , 5))
print(calculate(10 , 6))

print("Line 3")
print(calculate(10 , 0))

print("Line 4")
print("Line 5")


print(calculate(20 , 0))
print(calculate(40 , 0))
print(calculate(40 , 0))
