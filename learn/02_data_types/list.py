# list is ordered, changeable, allow duplicates
# cars = ['bmw', 'volvo']
cars = list(('bmw', 'volvo'))
# print(len(cars))
print(cars)
# access
print(cars[0:2])
print(cars[0:])
print(cars[:2])
print(cars[1])
if 'bcw' in cars:
    print('bmwwwww')

# change
cars[0] = 'volvo'
cars[0:2] = ['toyota', 'fortune']
cars[0:2] = ['single']
print(cars)
cars.insert(1, 'o yeah')
print(cars)

# add
cars.append('last')
cars.insert(1,'last2')
this_tuple = ('hell', 'heaven')
cars.extend(this_tuple)
print(cars)

# remove
cars.remove('hell')
cars.pop(4)
cars.pop()
del cars[1]
# del cars
# cars.clear()
print(cars)

# Loop
for car in cars:
    print(car)

# sort
# cars.sort(reverse=True)
#  case insensitive
# cars.sort(key=str.lower)
# cars.sort()
cars.reverse()
print(cars)

# copy
# cars_copy = cars.copy()
# cars_copy = list(cars)
cars_copy = cars[:]
print(cars_copy)

# join
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# list3 = list1+list2
# for char in list1:
#     list2.append(char)
list2.extend(list1)
print(list2)