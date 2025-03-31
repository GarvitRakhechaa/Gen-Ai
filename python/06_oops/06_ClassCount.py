# 6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

class Car():
    totalCar = 0
    def __init__(self, userBrand, userModel):
        self.brand = userBrand
        self.model = userModel
        Car.totalCar += 1
    
class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

Car("tata","dfkn") # car class nhi bna rhi hai ye constructure call kar rhi hai jitni baar call hoga utni baar 1 add hota jayega
Car("tata","dfkn")
Car("tata","dfkn")

print(Car.totalCar)