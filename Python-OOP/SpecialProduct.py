from Product import Product


class SpecialProduct(Product):
    def get_offer(self,product):
        return product.price *0.9

product1 = SpecialProduct('iPhon 12', 'This is a great iPhone', 799.0)
print(product1.get_offer(product1))