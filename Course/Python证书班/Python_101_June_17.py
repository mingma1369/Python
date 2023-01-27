# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 10:12:02 2018

@author: james
"""

#%% 

f = open("temp.txt")    


#%% Write to a file

fileName="GuestList.txt" 
accessMode="w" 
myFile=open(fileName,accessMode)
myFile.write("Hi there!")
myFile.write("How are you?")


#%%

fileName = "GuestList.txt" 
accessMode = "w" 
myFile = open(fileName, accessMode) 
myFile.write("Hi there!\n")
myFile.write("How are you?")
myFile.close()


#%%
import csv

fileName = "GuestList.txt"
accessMode = "r" 
with open(fileName, accessMode) as myCSVFile:     	#Read the file contents
	dataFromFile = csv.reader(myCSVFile)


#%% Define functions

def print_quote(): # header
    print("all work no play makes James?")
    print("a dull boy.")


#%% nested fuctions
    
def repeat_quotes():
    print_quote()
    print_quote()

#%% define functions with arguments
    
def print_your_quote(Name): # header
    first = "all work no play makes "
    second = Name
    third = "?"
    print(first + second + third)
    print("a dull boy.")
    

#%%
    
print_your_quote('Jack')


#%%

def print_your_quote(Name,Name2, Name3): # header
    first = "all work no play makes "
    second = Name
    third = "?"
    print(first + second + third)
    print("a dull boy.")
    
    print(Name2 + ' is a good girl')
    print(Name3 + ' is a good boy')
    
    
#%% use different variable names

xxx = 'James'
yyy = 'Grace'
zzz = 'Kelly'
    
print_your_quote(xxx,yyy, zzz)

#%% default argument

def greet(name, msg = "Good morning!"):
   """
   This function greets to the person with the
   provided message. If message is not provided,
   it defaults to "Good morning!"
   """
   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")


#%%

def justry(name, msg = 10):
   """
   This function greets to the person with the
   provided message. If message is not provided,
   it defaults to "Good morning!"
   
   """
   power = 2**msg
   
   print("Hello",name + ', ' + str(power))

#%%
justry("Kate")
justry("Bruce",20)

#%% Arbitrary Arguments


def greet(*names):
   """This function greets all
   the person(s) in the names tuple."""
   
# This function grees all
# the person(s) in the names tuple   

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","John", 'James', 'Husky')


#%% doc string

def greet(*names):
   """
   Version number: 1.0.01
   Date: June 17, 2018
   Author: James W. Jiang
   Production: No
   Validation: No
   Debugged: Twice
   
   This function greets all
   the person(s) in the names tuple."""
    

   # names is a tuple with arguments
   for name in names:
       print("Hello",name)

greet("Monica","Luke","John", 'James', 'Husky')

#%% Recursion

n = 10

def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)
        
        
#%% Factorial
        
def calc_factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    
    elif x == 0:
        
        return 1
    elif x < 0 :
        
        print('Input is negative')
    
    else:
        return (x * calc_factorial(x-1))

num = -5

print("The factorial of", num, "is",calc_factorial(num))

#%% return values

import math

def area(radius):
    a = math.pi * radius**2
    return a

r = 10
area_eg = area(r)

print('The area of the circle is', area_eg)

#%%

import math

def area(radius):
    a = math.pi * radius**2
    circ = 2*math.pi*radius
    return a, circ

#%%
r = 10
Answer = area(r)

print('The area of the circle with a radius of', r, ' is', Answer[0])
print('The peripheral of the circle with a radius of', r ,' is', Answer[1])


#%% 

#-------------------
def my_func():
	x = 10 # local variable 
	print("Value inside function:",x)
#------------------

# main function
    
x = 20
my_func()
print("Value outside function:",x)

#%% lambda function

double = lambda x: x * 2

# Output: 10
print(double(5))


#%%

class Parrot:
    
    '''This is a docstring. This is the introduction for a class
    called Parrot. Parrot currently has two members, Blu and Woo'''


    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#%%
# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

#%%

class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')
# Output: 10
print(MyClass.a)
# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)
# Output: 'This is my second class'
print(MyClass.__doc__)


#%%

class ComplexNumber:
    def __init__(self,r = 0,i = 0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))

# Create a new ComplexNumber object
c1 = ComplexNumber(2,3)

# Call getData() function; Output: 2+3j
c1.getData()

#%%

class Parrot:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    
    
    
# instantiate the object
blu = Parrot("Blu", 10)
# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

#%% multiple statements on a single line

x = 'boy'; y = 'friend'; print(x + y)

x = 'boy'
y = 'friend'
print(x + y)

#%% Line continuation

x = 'boy'; y = 'friend'
total = x + \
        y + \
        ' add as many lines as you want'
print(total)


a = 1 + 2 + 3 + \ # ... (Matlab)
    4 + 5 + 6 + \
    7 + 8 + 9

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

#%% improve readability

a = b + c; # It performs an addition
# Reference: 'Market Derivatives, second edition' McDonald
# Michael Lewis: Liar's Poke, Big Short, Moneyball

#-------------------- Step 1: Inialization 



#-------------------- 

xxxyyyyzzzz = zzzz + xxxx;

Noise_Base = Noise_source_1 + Noise_source_2; #at the same frequency, unit: W

Noise_Base

NoiseBase

#%% Runtime Errors, no handling


first = input("Enter the first number ") 
second = input("Enter the second number ") 
firstNumber = float(first) 
secondNumber = float(second) 
result = firstNumber / secondNumber
print(first + " / " + second + " = " + str(result))

#%% with error handling


first = input("Enter the first number ") 
second = input("Enter the second number ") 
firstNumber = float(first) 
secondNumber = float(second) 
try :
     result = firstNumber / secondNumber
     print(first + " / " + second + " = " + str(result))
except :
     print("I am sorry something went wrong")
     
     
#%% Know the error type

import sys 

first = input("Enter the first number ") 
second = input("Enter the second number ") 
firstNumber = float(first) 
secondNumber = float(second) 
try :
    result = firstNumber / secondNumber
    print (first + " / " + second + " = " + str(result))
except :
    error = sys.exc_info()[0] # tuple 
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
    print("I am sorry something went wrong")
    print(error)


#%% 
first = input("Enter the first number ") 
second = input("Enter the second number ") 
firstNumber = float(first) 
secondNumber = float(second) 
try :
    	result = firstNumber / secondNumber
    	print (first+" / "+second+" = "+str(result))
except ZeroDivisionError :
    	print("The answer is infinity")
    	print(ZeroDivisionError)


#%%


first = input("Enter the first number ") 
second = input("Enter the second number ") 
firstNumber = float(first) 
secondNumber = second
try :
    	result = firstNumber / secondNumber
    	print (first + " / " +second+ " = "+str(result))
except ZeroDivisionError :
    	print("The answer is infinity")
except :
	error = sys.exc_info()[0]
	print("I am sorry something went wrong")
	print(error)

#%% exit sys
    
try :
    result = firstNumber/secondNumber
    print (first+" / " +second + " = " + str(result))
except ZeroDivisionError :
    
    print("The answer is infinity")
    sys.exit() 
    
print("This message only displays if there is no error!")


xxx_flag = True # default value

if x < 10:
    
    xxx_flag = False

while xxx_flag:
    
    XXXXX
    
#%%
    
firstNumber = 10
secondNumber = 0

try :
    result = firstNumber / secondNumber
    print (first+" / " + second + " = " + str(result))
    errorFlag = False # default value
except ZeroDivisionError :
    print("The answer is infinity")
    errorFlag = True
if not errorFlag :  
	print("This message only displays if there is no error!") 


#%% Find prime numbers
    
# Python program to display all the prime numbers within an interval

# change the values of lower and upper for a different result
lower = 900
upper = 1000

# uncomment the following lines to take input from the user
#lower = int(input("Enter lower range: "))
#upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1): # test
    
    # A: range(lower,upper + 1)
    # B: range(lower,upper)
    # C: range(lower,upper - 1)
    
    
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               
               # (num % i) == 0
               # (num % i) == 1
               # (num % i+1) == 0
               
               break
       else:
           print(num)

#%% calculate sum

# local function:           
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

# Main function
    
print('The sum is',listsum([1,3,5,7,199]))


#%% calculate sum using recursion

def listsum(numList):
   if len(numList) == 1:
        return numList[0]
   else:
        return numList[0] + listsum(numList[1:])

print('The sum is',listsum([1,3,5,7,199]))


#%% Sorting algorithm

def shortBubbleSort(alist):
    exchanges = True # flag: default value
    passnum = len(alist)-1
    # question:
    # A: len(alist)-1
    # B: len(alist)
    # C: len(alist)+1
    
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
               # Put them in the right order
               #temp = alist[i]
               #alist[i] = alist[i+1]
               #alist[i+1] = temp
               
       passnum = passnum-1

alist=[20,15,66,88,55,5,77,8,3,111]
shortBubbleSort(alist)
print(alist)

#%%

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location # switch index

# switch values ----------------------
               
       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       
# switch values ----------------------       

alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


#%%

for i in range(10,0,-1):
    
    print('The value is',i)
    
    
    #%%
for i in range(10):
    
    print('The value is',i)

#%% Factorial
    
    
# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 5

# uncomment to take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i # no recursion
   print("The factorial of",num,"is",factorial)

#%%

# Python program to check if the input year is a leap year or not

year = 1900

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
    
#%%
   
year = 2005
   
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    
    print("{0} is a leap year".format(year))
else:
    
    print("{0} is not a leap year".format(year))

print('Done')

#%% Fibonacci

# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 100

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1 # a must: count = count + 1
       
#%% least common multiple

# Python Program to find the L.C.M. of two input number

# define a function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

# change the values of num1 and num2 for a different result
num1 = 54342
num2 = 2423

# uncomment the following lines to take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
       

#%%

# Python Program to find the factors of a number

# define a function
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

# change this value for a different result.
num = 50000

# uncomment the following line to take input from the user
#num = int(input("Enter a number: "))

print_factors(num)
       
