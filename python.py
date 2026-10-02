# Generator: generator is a function that uses the yield keyword instead of return and it is sending the values one
#            by one and also it is used for large data sects and more efficient sending the values vales at once

# def data():
#     yield 1
#     yield 2
#     yield 3

# number = data()
# print(next(number)) 
# print(next(number)) 

# ---------------------------------------------------------------------------------------------------------

# Difference between Python and Java ?

# Python is a dynamically typed, high-level programming language known for its simple syntax, while 
# Java is a statically typed, object-oriented language that runs on the JVM.

# ------------------------------------------------------------------------------------------------------- 
# Mutable and Immutable Objects 

# Mutable

# List
# Dictionary
# Set

# data = [10, 20, 30]
# data[0] = 100
# print(data)
# o/p = [100, 20, 30]

# Immutable

# Integer
# Float
# String
# Tuple
# Boolean

# name = "Anil"
# name[0] = "B"   # Error

# -----------------------------------------------------------------------------------------------------------

# What are decorators in Python?
# A decorator is a function that is used to add extra functionality to another function without changing 
# its original code

# def decorator(func):
#     def wrapper():
#         print("Before function")
#         func()
#         print("After function")
#     return wrapper

# @decorator
# def hello():
#     print("hello anil")
# hello()
# -------------------------------------------------------------------------------------------------------

# Difference between __init__ and int ?
# __init__ is a special method used in classes. It is called automatically when an object is created.

# class Student:
#     def __init__(self, name):
#         self.name = name

# s = Student("Anil")
# print(s.name)

# int() is a built-in function used to convert a value into an integer.

# x = "10"
# print(int(x))
# o/p = 10
# -------------------------------------------------------------------------------------------------------------

# Compiler vs Interpreter

# Compiler:

# Translates the program before execution.
# Generally translates the source code into another executable/intermediate form.
# Reports compilation errors before execution proceeds.

# Interpreter:

# Executes code through a runtime/interpreter.
# Traditionally described as executing code line by line, although modern runtimes may use bytecode, 
# JIT compilation, etc.
# -----------------------------------------------------------------------------------------------------------

# What is a Lambda Function?
# A lambda function is a small anonymous function written using the lambda keyword.

# Syntax:
# lambda arguments: expression

# Example:
# square = lambda x: x * x
# print(square(5))
# Output:
# 25
#        or
# data =lambda a,b:a+b
# print(data(4,2))
# -------------------------------------------------------------------------------------------------------------

# Exception Handling ?
# Exception handling is the process of detecting, handling, and responding, to the runtime errors.
# so the program can run smoothly instead of crashing.

# try:
#     num1 = int(input("enter any number:"))
#     num2 = int(input("enter any number:"))

#     res = num1/num2
#     print("result is :",res)

# except ZeroDivisionError:
#     print("can not divide by zero")
# except ValueError:
#     print("please provide only number")   
# -------------------------------------------------------------------------------------------------------------

# File Handling ?
# file handling is process in python to store the values in files permanently and retrive it whenever needed.
# and file handling have some functions like Write(),Read(),Append(),and Close() instead of close function we can
# use with keyword so no need to close the function is automatically closes.

# with open("anil.txt","w") as ab:
#     ab.write("hii anil \n")
# with open("anil.txt","a") as ab:
#     ab.write("how are you \n")
#     ab.write("i am good")
# with open("anil.txt","r") as ab:
#     print(ab.read())
# -------------------------------------------------------------------------------------------------

# Find out Even num or odd num ?

# num = int(input("enter any number:"))
# if num % 2==0:
#     print(num,"is Even number")
# else:
#     print(num,"is Odd number")
# --------------------------------------------------------------------------------------------------

# print prime number or not ?

# n = int(input("enter any number:"))
# if n<=1:
#     print(n,"Is Not a prime number")

# else:
#     for i in range(2,n):
#         if n % i == 0:
#             print(n,"Is Not a prime number")
#             break
#     else:
#         print(n,"Is a prime number") 
# -----------------------------------------------------------------------------------------------------------
# star angled triangle program

# for i in range(1,6):
#     for j in range (i):
#         print("*",end=" ")
#     print()

# star angled riverse
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# print particular number is prime or not ? like ex:23

# n=22
# count=0
# for i in range(1,n+1):
#     if n % i==0:
#         count+=1
# if count==2:
#     print(n,"is a prime number")
# else:
#     print(n,"is not a prime number")
# -----------------------------------------------------------------------------------------------
# print 1 to 100 prime numbers ?

# for n in range(2,101):
#     count =0
#     for i in range(1,n+1):
#         if n % i ==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")
# ------------------------------------------------------------------------------------------------------

# print prime numbers B/W 10 to 50 ?
# for n in range(10,51):
#     count=0
#     for i in range(1,n+1):
#         if n % i ==0:
#             count+=1
#     if count==2:
#         print(n,end=" ")
# --------------------------------------------------------------------------------------
