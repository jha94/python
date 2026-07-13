# Syntax, multiple args, polymorphism, return multiple values
# default parameter, lambda function, *args, **kwargs, generator, recursion 

# def square(number):
#     return number*number
# print(square(7))

# def sum(num1, num2):
#     return num1+num2
# print(sum(1,2))

# def poly(p1,p2):
#     return p1*p2
# print(poly(5,5))
# print(poly('a',5))
# print(poly(5,'a'))

# import math
# def circle_dim(radius):
#     area = math.pi*radius**2
#     circumference = 2*math.pi*radius
#     return area, circumference
# a,c = circle_dim(3)
# print(a)
# print(c)

# def sum(a,b=2):
#     return a+b
# print(sum(3,4))

# cube = lambda x:x**3
# print(cube(3))

# def sum_all(*args):
# def sum_all(*chai):
#     for x in chai:
#         print(x)

# sum_all(1,2)
# sum_all(1,2, 4, 5)

# def print_kwargs(name, power):
#     print("Name: ", name, "Power: ", power)

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ':', value)
# print_kwargs(name='Prashant', power='laser')
# print_kwargs(name='Prashant')
# print_kwargs(name='Prashant', power='laser', enemy='all')

def factorial(n):
    if(n<=1):
        return  1
    return n*factorial(n-1)
print(factorial(4))