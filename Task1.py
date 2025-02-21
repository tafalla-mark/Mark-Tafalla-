class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand} {self.model}, Year: {self.year}")

# Create two car objects
car1 = Car("BMW", "i8", 2015)
car2 = Car("BMW", "3.0CSL", 2018)

car1.display_info()
car2.display_info()
