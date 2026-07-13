age = 20
# if age>=18:
#     print("eligibale to bote")
# if age>18:print('eligible to vote')
if age>20:
    print('eligible to vote')
else:
    print('not eligible to vote')
if age<=12:
    print("child")
    if age<=8:
        print('less than 8')
    else:
        print('greater than 8')
elif age<=19:
    print("teen")
elif age<=35:
    print("young adult")
else:
    print("adult")

name = "harish" if age<=2 else "sandeep"
print(name)

# match age:
#     case 12:
#         print("12")
#     case 13:
#         print("13")
#     case _:
#         print('other')