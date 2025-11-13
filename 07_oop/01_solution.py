class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_cars += 1    

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "This is a general description of a car."        
        
    @property    
    def model(self):
        return self.__model
        

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

# my_car.model = "Camry"

print(my_car.model)

# print(my_tesla.fuel_type())
# print(my_car.fuel_type())

# print(my_car.general_description())
# print(Car.general_description())

# print(Car.total_cars)

# print(my_car)
# print(my_car2)
# print(my_car3)
# print(my_car.brand)
# print(my_car.model)

# print(my_car.full_name())
# print(my_car2.full_name())
# print(my_car3.full_name())  


# print(isinstance(my_car, Car))
# print(isinstance(my_car, ElectricCar))
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

class Battery:
    def battery_info(self):
        return "Battery Info"

class Engine:
    def engine_info(self):
        return "Engine Info"


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_tesla_two = ElectricCarTwo("Tesla", "Model S")
print(my_tesla_two.battery_info())
print(my_tesla_two.engine_info())
print(my_tesla_two.full_name())