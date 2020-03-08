class Seller:
    def __init__(self):
        self._self = self
        self.name = name
        self.salary = salary
        self.sales = sales

Seller.name = str(input())
Seller.salary = float(input())
Seller.sales = float(input())
bonus = 0.15
sales_total = Seller.sales*bonus
total = Seller.salary + sales_total
print("TOTAL = R$ {:.2f}".format(total))