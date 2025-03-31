# 10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

class Battery:
    pass

class Engine:
    pass

class ELectric_Car(Battery,Engine):
    pass

my_bettery = Battery()
my_engine = Engine()
my_ev_car = ELectric_Car()

print(isinstance(my_bettery, Battery)) #true
print(isinstance(my_ev_car, Battery)) #true
print(isinstance(my_engine, Engine)) #true
print(isinstance(my_ev_car, Engine)) #true
print(isinstance(my_ev_car, ELectric_Car)) #true
print(isinstance(my_engine, Battery))  #false
print(isinstance(my_bettery, Engine)) #false
print(isinstance(my_bettery, ELectric_Car)) #false
print(isinstance(my_engine, ELectric_Car)) #false
