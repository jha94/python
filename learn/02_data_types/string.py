# a = """fghjkl
# fghjkl
# dfghjk
# dfghjkl"""

# a = '''fghjkl
# fghjkl
# dfghjk
# dfghjkl'''
# print(a)

a = 'Hello world'
# print(a[1])
# for x in a:
#     print(x)
print(len(a))
print("hello" not in "hello world")

# Slice
print(a[2:5])
print(a[:5])
print(a[2:])

# modify
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('Hello', 'hi'))
print(a.split(' '))

# concate
a = 'hi'
b = 'ji'
print(a+' '+b)

# format
a = 10
b = 20
print(f"Sum of a and b is {a+b}")