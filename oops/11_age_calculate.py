
from datetime import datetime, date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

    def calculate_age(self):
        today = date.today()
        age = today.year - self.birthdate.year
        return age

person = Person("Alice", "2006-05-25")
print(f"{person.name} is {person.calculate_age()} years old.")
