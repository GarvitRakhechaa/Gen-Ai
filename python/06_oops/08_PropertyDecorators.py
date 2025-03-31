# 8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

class Car():
    def __init__(self, userBrand, userModel):
        self.__brand = userBrand
        self.__model = userModel

    @property
    def model(self):
        return self.__model
    
my_car = Car("tata","nexon")

print(my_car.model)
# my_car.model = "safari"
print(my_car.model)

# readonly ke liye @property use karo 
# mathod bna lo us property ka and @property will treat that mathod as property of class but value under this mathod must be private