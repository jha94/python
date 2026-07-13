# ordered, changeable and do not allow duplicate

car = {
    'brand':'ford',
    'model':'mustang',
    'year':1984
}
print(len(car))

# access
print(car['year'])
print(car.get('brand'))
print(car.keys())
print(car.values())
print(car.items())
car['year'] = 2020
print(car)

# add
# car['color'] = 'red'
car.update({'color':'red'})
print(car)

# remove
# car.pop('color')
# car.popitem()
# del car['color']
# car.clear()
# del car
print(car)

# for item in car:
#     print(f"{item}:{car[item]}")
# for item in car.values():
#     print(item)
# for item in car.keys():
#     print(item)
# for key, value in car.items():
#     print(f"{key}:{value}")

# copy
car_copy = car.copy()
car_copy = dict(car)
print(car_copy)