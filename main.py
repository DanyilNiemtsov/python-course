#  ! variables
# first_name = "bro "
# last_name = "code"
# full_name = first_name + last_name
# print("Hello", full_name)
# print(type(name))

# age = 21
# age += 1
# print("your age is: "+str(age))
# #print(type(age))

#? string, ints, float, bool
#! multiple assignment
# name = "bro"
# age = 21
# attractive = True
 
# name, age, attractive = "bro", 21, True

# print(name)
# print(age)
# print(attractive)
#! string methods
# name = "bro code"

# print(len(name))
# print(name.find("b"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o","a"))
# print(name*3)
#! type cast
# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# x = str(x)
# y = str(y)
# z = str(z)

# print(z*3)
# print(y)
# print(x)
#! user input
# age = input("what is your age?: ")

# print(21+int(age))
#! math functions
# import math

# pi = -3.14
# x = 1
# y = 2
# z = 3

# print(round(pi)) # round
# print(math.ceil(pi)) # round top
# print(math.floor(pi)) # round bottom
# print(abs(pi)) # absolute value
# print(pow(pi,2)) # power
# print(math.sqrt(420)) # squareroot
# print(max(x,y,z)) # max value
# print(min(x,y,z)) # min value
#! string slicing
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# name = "Bro Code"

# first_name = name[:3]
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name[::-1]

# print(reversed_name)

# website = "http://google.com"
# website = "http://wikipedia.com"
# slice = slice(7,-4)

# print(website[slice])
#! if statements
# age = int(input("how old are you?: "))

# if age >= 18:
#     print("you are an adult")
# elif age < 0:
#     print("you haven't been born!")
# else:
#     print("you are a child")
#! logical operators
# temp = int(input("Whta is the tempeture outside?: "))

# if not(temp >=0 and temp <= 30):
#     print("the temperature is bad today")
# elif not(temp < 0 or temp > 30):
#     print("the temperature is good today")
#! while loops
# while 1==1:
#     print("help! im stuk in a loop!")

# name = ""

# while not name:
#     name = input("Enter your name: ")

# print("hello", name)
#! for loops
# import time
# for i in range(10):
#     print(i+1)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Bro Code":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("happy new Year!")
#! nested loops
# rows = int(input("how many rows?: "))
# columns = int(input("how many colums?: "))
# symbol = input("Enter a ymbol to use: ")

# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()
#! break continue pass
# while True:
#     name = input("Enter your name!: ")
#     if name !="":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="") 

# for i in range(1, 21):

#     if i == 13:
#         pass
#     else:
#         print(i)
#! lists
# food = ["pizza", "hamburger", "hotdog", "spaghetti"]

# food[0] = "sushi"
# print(food[0])
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()

# for x in food:
#     print(x)
#! 2D lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[2][1])
#! tuples
# student = ("bro", 21, "male")

# print(student.count("bro"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "bro" in student:
#     print("bro is here!")
#! sets
# utensils = {"fork", "spoon","knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)
#! dictionary
# capitals = {'USA':'Washington DC',
#             'india':'New Dehli',
#             'China':'beijing',
#             'Russia':'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key,value in capitals.items():
#      print(key, value)
#! indexing
# name = "bro Code!"

# if(name[0].islower()):
#     name = name.capitalize()

# first_name = name[:3].upper()
# last_name = name[4:8].lower()
# last_character = name[-1]

# print(first_name, last_name + last_character)
#! functions
# def hello(first_name, last_name, number):
#     print("hello "+ first_name +" "+ last_name + " " + str(number))
#     print("have a nice day!")

# my_name = "bro"

# hello("Bro", "Code", 21)
#! return statement
# def multiply(number1, number2):
#     return number1 * number2

# x = multiply(6, 8)

# print(x)
#! Keyword arguments
# def hello(first, middle, last):
#     print("hello "+first+" "+middle+" "+last)

# hello(last="bro", middle="dude", first="code")
#! nested function calls
# num = input("enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("enter a whole positive bumber: ")))))
#! variable scope
# name = "bro" #? global scope

# def display_name():
#     name = "code" #? lосаl scope (available опlу inside this function)
#     print(name)

# display_name()
# print(name) #? eror without globol scope
#! args
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[1] = 0
#     for i in stuff:
#         sum += i
#     return sum

# print(add(2,3,4,5,6))
#! kwargs
# def hello(**kwargs):
#     # print("hello " + kwargs['first'] + " " + kwargs['last'])
#     print("hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")

# hello(first="Bro", middle="Dude", last="Code")
#! string format
# animal = "cow"
# item = "moon"

# # print("the "+animal+" jumped over the "+ item)
# # print("The {} jumped over the {}".format(animal,item))
# # print("The {1} jumped over the {0}".format(animal,item)) #positinal argument
# # print("The {item} jumped over the {animal}".format(animal="cow",item="moon")) #kw arguement

# text = "The {} jumped over the {}"
# print(text.format(animal,item))

# name = "Bro"

# print("hello, my name is {}".format(name))
# print("hello, my name is {name:10} nice to meet you".format(name)) #padding
# print("hello, my name is {:>10} nice to meet you".format(name)) #padding
# print("hello, my name is {:^10} nice to meet you".format(name)) #padding
# print("hello, my name is {:<10} nice to meet you".format(name)) #padding

# number = 1000

# print("The number pi is {:.3f}".format(number))
# print("The number pi is {:,}".format(number))
# print("The number pi is {:b}".format(number))
# print("The number pi is {:o}".format(number))
# print("The number pi is {:x}".format(number))
# print("The number pi is {:e}".format(number))
#! random numbers
# import random

# x = random.randint(1,6)
# y = random.random()

# mylist = ['rock','paper','scissors']
# z = random.choice(mylist)

# cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

# random.shuffle(cards)

# print(cards)
#! exception handeling 
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers: pls")
# except Exception as e:
#      print(e)
#      print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("kakka")
#! file detection
# import os

# path = "C:\\Users\\Danyi\\OneDrive\\Documents\\programing\\github\\Vaultnote"

# if os.path.exists(path):
#     print("that location exsists!")
#     if os.path.isfile(path):
#         print("that is a file")
#     elif os.path.isdir(path):
#         print("that is directory!")
# else:
#     print("that location not exsists")
#! read a file
# try:
#     with open('test.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("not found")
#! write a file
# text = "\nHave a nice day! see ya"

# with open('test.txt','a') as file:
#     file.write(text)
#! copying a file 
# import shutil

# shutil.copyfile('test.txt','copy.txt') #src.dst
#! move a file
import os

# source = "copy.txt"
# destination = "C:\\Users\\Danyi\\OneDrive\\Documents\\copy.txt"

# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source +" was moved")
# except FileNotFoundError:
#     print("not found")

# source = "folder"
# destination = "C:\\Users\\Danyi\\OneDrive\\Documents\\folder"

# try:
#     if os.path.exists(destination):
#         print("there is already a file there")
#     else:
#         os.replace(source,destination)
#         print(source +" was moved")
# except FileNotFoundError:
#     print("not found")
#! delete a file
import os

path = "copy.txt"

os.remove(path)