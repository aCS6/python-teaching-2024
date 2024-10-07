class Person:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
    
    def institution_address(self):
        print("European It. Mirupur-10")
    
    def working_hour(self):
        print('From 12 AM to 9PM')

class Student(Person):
    def __init__(self, name, email , student_id , course_name) -> None:
        super().__init__(name=name,email=email)
        self.student_id = student_id
        self.course_name = course_name
    
    def intro(self):
        print(f"Name is : {self.name} | Admitted: {self.course_name}")


class Teacher(Person):
    def __init__(self, name , email , teacher_id , department) -> None:
        super().__init__(name=name, email=email)
        self.teacher_id = teacher_id
        self.department = department


p1 = Person(name="Harun", email="harun@abc.com")
# p1.institution_address()
s1 = Student(name="Sagor", email="sagor@abc.com", student_id="11223", course_name="wordpress")
# s1.institution_address()
t1 = Teacher(name="Nahid", email="nahid@abc.com", teacher_id="T1234", department='web development')
# t1.institution_address()


# p1.intro()
p1.working_hour()
s1.working_hour()
t1.working_hour()