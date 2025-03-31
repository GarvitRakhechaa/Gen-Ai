# 5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
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
    
    def get_fuelType(self):
        return "pattrol charge"
    
class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

    def get_fuelType(self):
        return "battery charge"

my_car = Car("tata", "fortuner")
my_ev = ElectricCar("tesla","x234","85lwatt")

print(my_ev.batterySize)
print(my_ev.model)
# print(my_car.model)
# print(my_ev.brand)
print(my_ev.get_brand())
my_ev.set_brand("roles")
print(my_ev.get_brand())


print("polimosphism example")
print(my_car.get_fuelType())
print(my_ev.get_fuelType())

            
    


