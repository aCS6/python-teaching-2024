class A:
    def __init__(self) -> None:
        print('A')
    
    def hello(self):
        print("hello from A")

class B(A):
    def __init__(self) -> None:
        super().__init__()
        print('B')
    
    def hello(self):
        print("Hello from B")

class C(A):
    def __init__(self) -> None:
        super().__init__()
        print('C')
    
    def hello(self):
        print('hello from C')

class D(B, C):
    def __init__(self) -> None:
        super().__init__()
        print('D')


d = D()

print(D.mro())

d.hello()