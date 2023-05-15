class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, {self.name}!"


class Client(User):
    def __init__(self, name, email, company):
        super().__init__(name, email)
        self.company = company

    def get_company_name(self):
        return f"Company: {self.company}"


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"Product: {self.name} | Price: {self.price}"


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def get_discounted_price(self):
        discounted_price = self.price - (self.price * self.discount)
        return f"Discounted Price: {discounted_price}"

