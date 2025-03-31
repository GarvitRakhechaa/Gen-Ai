# 7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.
class Car():
    def __init__(self, userBrand, userModel):
        self.__brand = userBrand
        self.model = userModel
    
    def display(self):
        print(f"{self.__brand},{self.model}")

    def get_brand(self):
        return self.__brand
    
    def set_brand(self, value):
         self.__brand = value 
    #@staticmethod  # ye lagau to self hatana padega and Car. se get kar sakte hai 
    # static mathod nhi hai to my_car se get hoga and self bhi lagana hoga 
    def general_description(self):
        return f"this is general descriptio of car"

    
class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

my_ev = ElectricCar("tata","safati","5000")
my_car = Car("tata","safati")

print(my_car.general_description())
# print(Car.general_description())


# my_car.  staticmathod hatao self lagao 
# Car.      staticmathod lagao self hatao