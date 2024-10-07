def calculate(number1, number2):
    return number1 / number2


print("Line 1")
print("Line 2")

print(calculate(10 , 5))
print(calculate(10 , 6))

print("Line 3")

try:
    # dangerous code
    print(calculate(10 , 0))
except:
    print("Error !")

print("Line 4")
print("Line 5")


try:
    # dangerous code
    print(calculate(20 , 0))
except:
    print("Error !")


try:
    # dangerous code
    print(calculate(40 , 0))
except:
    print("Error !")