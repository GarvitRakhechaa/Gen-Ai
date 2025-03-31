# 3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

class Car():
    def __init__(self, userBrand, userModel):
        self.brand = userBrand
        self.model = userModel
    
class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

my_ev = ElectricCar("tata","safati","5000")

print(my_ev.batterySize)
print(my_ev.model)
print(my_ev.brand)


            
    


