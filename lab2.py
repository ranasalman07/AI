# try:
#     x = int(input("Enter a number: "))
#     y = 10 / x
#     print("Result:" , y)
# except ValueError:
#     print("Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except Exception as e:
#     print("An error occured:" , e)



#==========================================
# with open("sample.txt" , "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a sample file.\n")
# with open("sample.txt" , "r") as file:
#     contents = file.read()
#     print("File Contents:")
#     print(contents)
# with open("sample.txt", "r") as file:
#     lines = file.readlines()
#     print("File Contents as List:")
#     print(lines)



#==========================================
# def add(a,b):
#     return a + b
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# numbers = [1,2,3,4,5]
# doubled_numbers = list(map(lambda x: x*2, numbers))
# print("Doubled Numbers:", doubled_numbers)
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print("Even Numbers:", even_numbers)
# squares = [x ** 2 for x in numbers]
# print("Squares:", squares)



#==========================================
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# person1 = Person ("Alice", 30)

# class Dog:
#     def __init__(self, name):
#         self.name = name
#     def bark(self):
#         return f"{self.name} says woof!"
    
# dog1 = Dog("Buddy")
# print(dog1.bark())

# class Animal:
#     def speak (self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"



#=====================================
# class Animal:
#     def make_sound(self):
#         pass
# class Dog (Animal):
#     def make_sound(self):
#         return "Woof!"
# class Cat (Animal):
#     def make_sound(self):
#         return "Meow!"
# class DogCat (Dog, Cat):
#     pass
# pet = DogCat()
# print(pet.make_sound()) 
# from abc import ABC, abstractmethod

# class Vehicle (ABC):
#     @abstractmethod
#     def move(self):
#         pass
# class Car(Vehicle):
#     def move(self):
#         return "Car is moving"



#=====================================
# class A:
#     def process(self):
#         return "A"
# class B(A):
#     def process(self):
#         return "B"
# class C(A):
#     def process(self):
#         return "C"
# class D(B, C):
#     pass
# print(D().process())



#=====================================
#LAB TASK
# with open("task.txt", "w") as file:
#     file.write("Hello World! \nThis is Salman here")
#     file.write("\nFrom UOL")
# with open("task.txt","r") as file:
#     contents=file.read()
#     print("File contents",contents)



#============================================
def read_file(file_name):
    
    with open(file_name, 'r') as f:
        file_contents = f.read()
        print(file_contents)
        return file_contents

def read_file_into_list(file_name):
 
    with open(file_name, 'r') as f:
        file_list = f.readlines()
        return file_list

def write_first_line_to_file(file_contents, output_filename):

    first_line = file_contents.split('\n')[0]
    with open(output_filename, 'w') as f:
        f.write(first_line)

def read_even_numbered_lines(file_name):

    with open(file_name, 'r') as f:
        file_list = f.readlines()
        even_numbered_lines = file_list[::2]
        return even_numbered_lines

def read_file_in_reverse(file_name):
  
    with open(file_name, 'r') as f:
        file_list = f.readlines()
        file_list.reverse()
        print(file_list)
        return file_list
def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")


