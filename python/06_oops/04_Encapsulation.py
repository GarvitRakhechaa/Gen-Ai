# 4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it. 


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
    
class ElectricCar(Car): # yha parent class ka name dedo
    def __init__(self,userBrand,userModel,userBatterySize): # car ke saare attrivutes to aayenge hi
        super().__init__(userBrand,userModel) # vlaues set to karni padegi hi but parent ke paas set hai to eha se lelenge es code se
        self.batterySize = userBatterySize #ye to ev ka hi aatrivute hai

my_ev = ElectricCar("tata","safati","5000")

print(my_ev.batterySize)
print(my_ev.model)
print(my_ev.brand)
print(my_ev.get_brand())
my_ev.set_brand("roles")
print(my_ev.get_brand())


            
    


