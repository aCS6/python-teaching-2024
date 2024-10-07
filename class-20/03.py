class Employee:
    def __init__(self, name) -> None:
        self.name = name

    def get_employee_details(self):
        print(f"Employee. Name: {self.name}")


class FullTimeEmployee(Employee):
    def __init__(self, name , monthly_salary):
        super().__init__(name=name)
        self.monthly_salary = monthly_salary
    
    # method overriding
    def get_employee_details(self):
        print(f"Full Time Employee. Name: {self.name}")
    

class PartTimeEmployee(Employee):
    def __init__(self,name, hourly_rate, total_hour):
        super().__init__(name=name)
        self.hourly_rate = hourly_rate
        self.total_hour = total_hour


f1 = FullTimeEmployee(name='Sahikb', monthly_salary="50000")
p1 = PartTimeEmployee(name='rakib', hourly_rate=100, total_hour=60)
p2 = PartTimeEmployee(name="Akram", hourly_rate=200, total_hour=40)

f1.get_employee_details()
p1.get_employee_details()
p2.get_employee_details()