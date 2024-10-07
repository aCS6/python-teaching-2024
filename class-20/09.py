class A:
    def __int__(self, number):
        self.number = number
    
    @classmethod
    def my_class_method(cls):
        value = cls.something()
        print("my class method - ", value)

    @staticmethod
    def my_static_method():
        print("my static method")

    @classmethod
    def something(cls):
        return 10
    
    
A.my_class_method()
A.my_static_method()