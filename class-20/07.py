class Base1:
    def __init__(self):
        print("Base-1 created")
    
    def method(self):
        print("from base-1")
    
    def greet(self):
        print("Hello")

class Base2:
    def __init__(self):
        print("Base-2 created")

    def method(self):
        print("from base-2")
    
    def hi(self):
        print("hi")

class Dervied(Base2, Base1):
    def __init__(self):
        super().__init__()
        print("Myself created!")


d = Dervied()

# 
d.method()


# MRO (Method Resolution Order)
print(Dervied.mro())