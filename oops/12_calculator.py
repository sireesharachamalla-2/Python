
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


c = Calculator()
print("Addition:", c.add(4, 5))
print("Division:", c.divide(10, 2))
