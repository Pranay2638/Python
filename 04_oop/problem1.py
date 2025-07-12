# Self - context to establish connection(telephone line) between class and object

class Car:
    # brand = None
    # model = None
    totalCar = 0
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model
        Car.totalCar += 1

    def get_brand(self): #Encapsulation
        return self.__brand + "!"

    def fullName(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self): # polymorphism
        return "Petrol or Diesel"

# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla","Model S", "85KWh")
print(my_tesla.fuel_type())

Car("Tata","Safari")
Car("Tata","Nexon")
print(Car.totalCar)
# print(my_tesla.get_brand())


# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())


