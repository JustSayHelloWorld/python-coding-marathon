"""Write the programm that calculate total price with discount by the products.

Use class Product(name, price, count) and class Cart. In class Cart you can add the products.

Discount depends on count product:


count	discount
2	0%
5	5%
7	10%
10	20%
20	30%
more than 20	50%
Write unittest with class CartTest and test all methods with logic"""

import unittest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:

    def __init__(self):
        self.cart = []
        self.total_to_pay = 0
        self.discount = 0
        self.goodscounter = 0
        self.instance_example = Product("as", 5, 6)

    def add(self, product):
        try:
            if type(product.name) is str:
                self.cart.append(product)
                self.goodscounter += product.count
                self.total_to_pay += product.price
        except:
            raise ValueError

    def calculate(self):
        if self.goodscounter > 20:
            self.discount = 50
        elif self.goodscounter == 20:
            self.discount = 30
        elif 10 <= self.goodscounter <= 19:
            self.discount = 20
        elif 7 <= self.goodscounter <= 9:
            self.discount = 10
        elif 5 <= self.goodscounter <= 6:
            self.discount = 5
        return self.total_to_pay - ((self.total_to_pay / 100) * self.discount)


class CartTest(unittest.TestCase):
    Product_apple = Product("apple", 32, 15)
    Product_mango = Product("mango", 12, 3)
    Product_cherry = Product("cherry", 15, 6)
    test_cart = Cart()
    test_cart.add(Product_apple)
    test_cart.add(Product_mango)
    test_cart.add(Product_cherry)

    Product_apple_1 = Product("apple", 32, 1)
    Product_mango_1 = Product("mango", 12, 1)
    Product_cherry_1 = Product("cherry", 15, 1)
    test_cart_2 = Cart()
    test_cart_2.add(Product_apple_1)
    test_cart_2.add(Product_mango_1)
    test_cart_2.add(Product_cherry_1)

    def test_discounted_price(self):
        expected = 29.5
        actual = self.test_cart.calculate()
        self.assertEqual(actual, expected)

    def test_add_not_product_to_cart(self):
        self.assertRaises(Exception, self.test_cart.add, "exected")

    def test_product_counter(self):
        expected = 24
        actual = self.test_cart.goodscounter
        self.assertEqual(actual, expected)

    def test_no_discount_price(self):
        expected = 59
        actual = self.test_cart_2.calculate()
        self.assertEqual(actual, expected)







