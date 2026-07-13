class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.model = model
        self.__brand = brand
        self.total_car+=1
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand
    def fuel_type(self):
        return 'petrol or diesel'
    @staticmethod
    def general_info():
        return 'cars are for transport'
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return 'electric cahrge'

car = Car('Mercedes', 'SLV')
print(car.general_info())
print(car.total_car)
print(car.get_brand())
print(car.full_name())
print(car.fuel_type())

e_car = ElectricCar('Mercedes', 'SLV', '3kWh')
print(e_car.full_name())
print(e_car.battery_size)
print(e_car.fuel_type())
# print(isinstance(e_car, Car))
# print(isinstance(e_car, ElectricCar))

class Battery:
    def battery_info(self):
        return 'batt info'
class Engine:
    def engine_info(self):
        return 'engine info'
    
class ElectricCar2(Battery,Engine, Car):
    pass
ec = ElectricCar2('test','test')
print(ec.battery_info())
