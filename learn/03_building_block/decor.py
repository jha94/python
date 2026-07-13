# import time
# def timer(func):
#     def wrap(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"ran in {end-start}")
#         return result
#     return wrap

# @timer
# def fun(n):
#     time.sleep(n)
# fun(2)

def details(func):
    def wrap(*args):
        print(func.__name__)
        print(args)
    return wrap

@details
def have_fun(name):
    print('enjoy', name)
have_fun('jha')