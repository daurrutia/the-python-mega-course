# import datetime
# print("The date and time is", datetime.datetime.now())

# mynow = datetime.datetime.now()
# print (mynow)

# mynumber = 10
# mytext = "Hello"

# print(mynumber, mytext)

# x = 10
# y = "10"
# z = 10.1

# sum1 = x + x
# sum2 = y + y

# print(sum1, sum2)
# print(type(x), type(y), type(z))

#######################################

# monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

# mysum = sum(student_grades.values())
# length = len(student_grades)
# mean = mysum / length
# print(mean)

# monday_temperatures = [8.8, 9.1, 9.9]

# def mean(value):
#      if isinstance(value, dict):
#           the_mean = sum(value.values()) / len(value)
#      else:
#           the_mean = sum(value) / len(value)
     
#      return the_mean

# print(mean(student_grades))

#######################################
# Conditionals

# def weather_condition(temperature):
#      if temperature > 7:
#           return "Warm"
#      else:
#           return "Cold"

# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))

#######################################
# String Formatting with Multiple Variables

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# when = "today"

# #message = "Hello %s %s!" % (name, surname)

# message = f"Hello {name} {surname}. What's up {when}?"

# print(message)

#######################################
# While loops

# username = ''

# while username != 'pypy':
#      username = input("Enter username: ")

#######################################
# While loops

# while True:
#      username = input("Enter username: ")
#      if username == 'pypy':
#           break
#      else:
#           continue

#######################################
# List comprehension

# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)

#######################################
#  List Comprehension with If Conditional

# temps = [221, 234, 340, -9999, 230]

# new_temps = [ temp / 10 for temp in temps if temp != -9999]

# print(new_temps)

#######################################
#  List Comprehension with If else Conditional

# temps = [221, 234, 340, -9999, 230]

# new_temps = [ temp / 10 if temp != -9999 else 0 for temp in temps ]

# print(new_temps)

#######################################
# Functions with Multiple Arguments

# def area(a, b):
#     return a * b

# print(area(4, 5))

#######################################
# Default and Non-default Parameters and Keyword and Non-keyword Arguments

# def area(a, b):
#      return a * b

# print(area(b=1, a=1))

#######################################
# Functions with an Arbitrary Number of Non-keyword Arguments

# def mean(*args):
#     return args

# print(mean(1, 3, 'a', 4))

#######################################
# Functions with an Arbitrary Number of Keyword Arguments

# def mean(**kwargs):
#      return kwargs

# print(mean(a=1, b=3, c='a', d=4))

#######################################
# Reading Text From a File

# myfile = open("fruits.txt")
# print(myfile.read())

#######################################
# File cursor

# myfile = open("fruits.txt")
# content = myfile.read()
# print(content)
# print(content)

#######################################
# Closing a file

# myfile = open("fruits.txt")
# content = myfile.read()
# myfile.close()

# print(content)

#######################################
# Opening Files Using "with"
# closes the file implicitly

# with open("fruits.txt") as myfile:
#     content = myfile.read()

# print(content)

#######################################
# Different Filepaths

# with open("files/fruits.txt") as myfile:
#     content = myfile.read()

# print(content)

#######################################
# Writing Text to a File

# with open("files/vegetables.txt", "w") as myfile:
#      myfile.write("Tomato\nCucumber\nOnion\n")
#      myfile.write("Garlic\n")

#######################################
# Appending Text to an Existing File

# with open("files/vegetables.txt", "a+") as myfile:
#      myfile.write("Okra\n")
#      myfile.seek(0)
#      content = myfile.read()

# print(content)

#######################################
# Builtin Modules

# import time

# while True:
#     with open("files/vegetables/txt") as file:
#         print(file.read())
#         time.sleep(10)

#######################################
# Standard Python Modules

# import time
# import os

# while True:
#     if os.path.exists("files/vegetables.txt"):
#         with open("files/vegetables/txt") as file:
#             print(file.read())
#     else:
#         print("File does not exist.")
#     time.sleep(10)

#######################################
# Third-Party Modules

# import time
# import os
# import pandas

# while True:
#     if os.path.exists("files/temps_today.csv"):
#         data = pandas.read_csv("files/temps_today.csv")
#         print(data.mean())
#     else:
#         print("File does not exist.")
#     time.sleep(10)

#######################################
#