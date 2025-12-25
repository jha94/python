class Car:
    def __init__(self, brand, model):
        # double __ before a variable, makes it private
        self.__brand = brand
        self.model = model
    def full_name(self):
        return self.__brand+" "+self.model
    def get_brand(self):
        return self.__brand+"!"

# car = Car('Toyota', 'Fortuner')
# print(car.brand)
# print(car.full_name())
# car = Car('Mercedes', 'G-Wagon')
# print(car.full_name())

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
tesla = ElectricCar('Tesla', 'X', '85kWH')
print(tesla.__brand)
print(tesla.get_brand())

