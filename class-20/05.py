class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("Works at ABC engineering")


class Employee(Person):
    def __init__(self, name , age, id):
        super().__init__(name=name, age=age)
        self.id = id

    def get_employee_details(self):
        print(f"Id- {self.id} | Name - {self.name}")

class Manager(Employee):
    def __init__(self, name, age, id, department):
        super().__init__(name=name , age=age, id=id)
        self.department = department
    
    def maneger_role(self):
        print(f"{self.name} is a nice manager of the department - {self.department}")

    
manager1 = Manager(name="xyz", age=30, id=123, department="HR")
manager1.intro()
manager1.get_employee_details()
manager1.maneger_role()

