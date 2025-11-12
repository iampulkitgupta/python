class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand + " !"
    
    def get_model(self):
        return self.__model
        

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
        

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric Charge"



my_tesla = ElectricCar("Tesla", "Model S", 75)
# print(my_tesla.full_name())
# print(my_tesla.battery_size)

# print(my_tesla.__brand)
# print(my_tesla.get_brand())




my_car = Car("Toyota", "Corolla")
my_car2 = Car("Honda", "Civic")
my_car3 = Car("Ford", "Mustang")

print(my_tesla.fuel_type())
print(my_car.fuel_type())



# print(my_car)
# print(my_car2)
# print(my_car3)
# print(my_car.brand)
# print(my_car.model)

# print(my_car.full_name())
# print(my_car2.full_name())
# print(my_car3.full_name())  


