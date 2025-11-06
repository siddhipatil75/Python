# Problem 2: Shopping Cart System

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def remove_product(self, product):
        if product in self.items:
            self.items.remove(product)

    def total_price(self):
        return sum(p.price for p in self.items)


# Polymorphism - Different Discounts
class Discount:
    def apply(self, total):
        return total


class PercentageDiscount(Discount):
    def __init__(self, percent):
        self.percent = percent

    def apply(self, total):
        return total - (total * self.percent / 100)


class FlatDiscount(Discount):
    def __init__(self, amount):
        self.amount = amount

    def apply(self, total):
        return total - self.amount


# Abstraction for Payment
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# --- Example Run ---
p1 = Product("Shoes", 1000)
p2 = Product("Bag", 500)

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)

print("Total Price:", cart.total_price())

# Apply discount
discount = PercentageDiscount(10)   # 10% off
final_price = discount.apply(cart.total_price())
print("Price after discount:", final_price)

# Payment
payment = UPIPayment()
payment.pay(final_price)
