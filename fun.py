# def fun():
#     print('we are having fun')
# fun()

# def add(a,b):
#     return a+b
# print(add(1,2))

# def mul(a,b):
#     return a*b
# print(mul(2,3))
# print(mul('a',3))
# print(mul(2, 'a'))

# def mulReturn():
#     return 'a' 'b'
# a, b = mulReturn()
# print(a)

# def default_param(a,b=10):
#     return a*b
# print(default_param(2))

# cube = lambda a:a**3
# print(cube(3))

# def max_count(count):
#     number = 0
#     while(number<count):
#         yield number
#         number+=1

# test = max_count(5)
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))
# print(next(test))

def test(n):
    if n<=0:
        print("done")
    else:
        print(n)
        test(n-1)

test(5)
