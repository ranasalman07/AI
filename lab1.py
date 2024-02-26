# integer_var = 10
# float_var = 3.14
# string_var = 'hello'
# boolean_var = True

# print("Integer Variable:",integer_var)
# print("Float Variable:",float_var)
# print("String Variable:",string_var)
# print("Boolean Variable:",boolean_var)

#=======================================

# integer_var = 10
# float_var = float(integer_var)
# print("Float Variable after Type Casting:",float_var)
# float_var = 3.14
# integer_var = int(float_var)
# print("Integer Variable after Type Casting:",integer_var)
# integer_var = 0
# string_var = 10
# string_var = str(integer_var)
# print("String Variable after Type Casting:",string_var)

#=======================================

# x = 10
# y = 3
# print("Addition:", x + y)
# print("Substraction:", x - y)
# print("Multiplication:", x * y)
# print("Division:", x / y)
# print("Modulus:", x % y)
# print("Exponentiation:", x ** y)

# a = True
# b = False
# print("AND:", a and b)
# print("OR:", a or b)
# print("NOT:", not a)

#=======================================

# x = 10
# if x > 0:
#     print("x is positive")
# else:
#     print("x is non-positive")

# y = -5
# if y > 0:
#     print("y is positive")
# elif y == 0:
#     print("y is zero")
# else:
#     print("y is negative")

#=======================================

# for i in range(5):
#     print(i)
# x = 0
# while x < 5:
#     print(x)
#     x+=1

#=======================================

# for i in range(3):
#     for j in range(2):
#         print(i,j)

#=======================================

# def greet(name):
#     return "Hello, " + name + "!"
# print(greet("Alice"))

#=======================================

# x = 10
# def my_function():
#     y = 20
#     print("Inside function:",x,y)
# my_function()
# print("Outside function:",x)

#=======================================

# fruits = ['apple','banana','orange']
# print(fruits[0])
# fruits[1] = 'grape'
# print(fruits)
# fruits.append('mango')
# print(fruits)

#=======================================

# days_of_week = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
# print(days_of_week[0])

#=======================================

# student = {'name': 'Alice', 'age': 20, 'grade':'A'}
# print(student['name'])
# student['age'] = 21
# print(student)
# student['city'] = 'New York'
# print(student)

#=======================================

# colors = {'red', 'green','blue'}
# colors.add('yellow')
# print(colors)
# colors.add('red')
# print(colors)

#=======================================

# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# greet(name="Alice", age=30)
