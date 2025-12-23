# list = [True,1,  "name", 1, [5,6]]
# print(len(list))
# print(list[-1])
# print(list[2:])
# print(list[:4])
# if("name" not in list):
#     print('yes, "name" is present in list')
# else:
#     print('hey')
# list[2] = "prashant"
# list[2:4] = ['6', '7', '8']
# list.insert(2, 'two')
# print(list)

# fruit_list = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)
# thislist.insert(2, "orange")
# car_list = ["lambo", "pagani"]
# fruit_list.extend(car_list)
# print(fruit_list)

# fruit_list.remove("cherry")
# fruit_list.pop()
# fruit_list.clear()
# print(fruit_list)

# fruit_a = [x for x in fruit_list if "a" in x]
# print(fruit_a)

# thislist = [100, 50, 65, 82, 23]

# thislist.sort().reverse()
# thislist.reverse()

# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# newList = thislist.copy()
# newList = list(thislist)
# newList = thislist[:]
# print(newList)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

# print(list1+list2)
list1.extend(list2)
print(list1)