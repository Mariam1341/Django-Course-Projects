class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

product1 = Product('iPhon 12', 'This is a great iPhone', 799.0)
print(product1.price)