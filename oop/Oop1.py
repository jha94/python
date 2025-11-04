# class Car:
#     # brand = None
#     # model = None
#     total_car = 0
#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
#         Car.total_car+=1
#     def full_name(self):
#         return self.__brand+' '+self.__model
#     def get_brand(self):
#         return self.__brand
#     def fuel_type(self):
#         return "Petro or Diesel"
#     @staticmethod
#     def general_description():
#         return "This is not an electric car"
#     @property
#     def model(self):
#         return self.__model



# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_size):
#         super().__init__(brand, model)
#         self.battery_size = battery_size
#     def fuel_type(self):
#         return "Electric Charge"

# my_car = Car('land rover', 'defender')
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.full_name())
# print(my_car.fuel_type())
# print(my_car.general_description())
# print(Car.general_description())
# my_car2 = Car('land rover', 'defender')
# print(Car.total_car)
# e_car=ElectricCar('mercedes','s-class','100kWH')
# print(isinstance(e_car, Car))
# print(isinstance(e_car, ElectricCar))
# print(e_car.battery_size)
# print(e_car.full_name())
# print(e_car.fuel_type())

class Engine:
    def engine_info(self):
        return "This is an engine"
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class ElectricCar(Engine, Battery):
    def car_info(self):
        return "this is car"

e_car = ElectricCar()
print(e_car.battery_info())
print(e_car.car_info())