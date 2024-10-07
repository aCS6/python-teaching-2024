class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
    
    def product_promotion(self):
        print(f"XYZ ecommerce is a relaible center for you. You can buy {self.name} at the best price {self.price}")

class Electronics(Product):
    def __init__(self, name, price, warranty, category) -> None:
        super().__init__(name=name , price=price)
        self.warranty = warranty
        self.category = category

class Clothing(Product):
    def __init__(self, name, price , size , type) -> None:
        super().__init__(name=name , price=price)
        self.size = size
        self.type = type


m1 = Electronics(name='Iphone13', price=87000, warranty=1, category="mobile")
l1 = Electronics(name='Asus Vivobook', price=70000, warranty=2, category='Laptop')
p1 = Clothing(name='Polo', price=1000, size='XXL', type='cotton')


m1.product_promotion()
l1.product_promotion()
p1.product_promotion()