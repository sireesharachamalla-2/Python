
class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add(self, item, quantity, price):
        if item in self.items:
            self.items[item][0] += quantity  
        else:
            self.items[item] = [quantity, price]

    def remove(self, item):
        if item in self.items:
            del self.items[item]

    def total(self):
        total_price = 0
        for item in self.items:
            quantity, price = self.items[item]
            total_price += quantity * price
        return total_price

    def display(self):
        for item, (qty, price) in self.items.items():
            print(qty*price)
cart = ShoppingCart()

cart.add("Book", 2, 200)  
cart.add("Pen", 5, 20) 

cart.display()
print("Total bill:", cart.total())
