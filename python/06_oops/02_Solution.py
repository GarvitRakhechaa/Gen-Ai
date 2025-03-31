# 2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

class Car:
    def __init__(self, userBrand, userModel):
        self.brand = userBrand
        self.model = userModel

    def display(self):
        print(f"{self.brand},{self.model}")
        
        


my_car =  Car("tata", "safari")

my_car.display()