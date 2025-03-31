# 9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car():
    def __init__(self, userBrand, userModel):
        self.__brand = userBrand
        self.model = userModel

class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

my_ev = ElectricCar("tesla","x","85k Watt")
my_car = Car("tata","nexon")

print(isinstance(my_ev, Car))
print(isinstance(my_ev, ElectricCar))
print(isinstance(my_car, Car))
print(isinstance(my_car, ElectricCar))