# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 10:07:47 2018

@author: James
"""

#%% Math operations

a = 5+2
print (a)
a = 5-2
print (a)
a = 5*2
print (a)
a = 5/2
print (a)
a = 5**2
print (a)
a = 5%2
print (a)

#%% calculation 

width = 20 
height = 5

area = width*height 

perimeter=2*width+2*height 

perimeter=2*(width+height) 

print ('The area is ', area)
print ('The perimeter is ', perimeter)

#%% Floor division

minutes = 105
hours = minutes // 60

#%% Relation

x = True
y = 1

x == y   # x is equal to y
type(x == y)
x is y

x != y   # x is not equal to y
x = True
y = 2

x >  y  # x is greater than y
x <  y   # x is less than y

x >= y   # x is greater than or equal to y
x <= y   # x is less than or equal to y
x <> y   # This is similar to != operator.

#%% Logical

x = 5

x > 0 and x < 10  
(x > 0) and (x < 10)  

x = 10

x > 0 and x < 10  

x = 15

x > 0 and x < 10  

n = 6

n%2 == 0 or n%3 == 0 

n = 8

n%2 == 0 or n%3 == 0 


#%%

x = True
y = False
# Output: x and y is False
print('x and y is',x and y)

# Output: x or y is True
print('x or y is',x or y)

# Output: not x is False
print('not x is',not x)


False or False

not(False or False)

not(False and False)

not(False and True)


not False or False

not False and False

not False and True

z = (2*7 + 8)**5 - 125

(z/365 + 123)*4

#%% Formatting

print('I have %d cats' % 6)

print('I have %3d cats' % 6)

print('I have %3d cats' % 16)

print('I have %03d cats' % 6)

print('I have %03d cats' % 16)

print('I have %f cats' % 6)

print('I have %.2f cats' % 6)

print("I have {0:d} cats".format(6)) # 0: the first element

print("I have {0:3d} cats".format(6)) 

print("I have {0:03d} cats".format(6)) 

print("I have {0:f} cats".format(6)) 

print("I have {0:.2f} cats".format(6)) 

#%% Conversion


salary=input("Please enter your salary: ")
type(salary)
bonus=input("Please enter your bonus: ")
type(bonus)

payCheck=salary+bonus # str plus str
print(payCheck)

#%% Conversion, updated

salary = input("Please enter your salary: ")
bonus = input("Please enter your bonus: ")
# payCheck = salary + bonus
payCheck = float(salary) + float(bonus)
print(payCheck)

#%% Assignment operations

x = 5
x+= 10 # x = x + 10
print(x)


x = 5
x*= 10 # x = x + 10
print(x)

x = 5
x/= 10 # x = x + 10
print(x)

#%% Bitwise 


a = 0b00111100
b = 0b00001101
#   0b00001100
# 0*2**0 + 0*2**1 + 1*2**2 + 1*2**3
a = 0b00111100
b = 0b00001101
111101

bit_AND = a & b
bit_OR = a | b

#%% Membership

a = 10
b = 20
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
   print "Line 1 - a is available in the given list"
else:
   print "Line 1 - a is not available in the given list"


#%%
   
True is 1
True is 1.0
True == 1
1 == True
True == 2
False is 0
False == 0
False == 0.0
True + 1
int(True)
float(True)
int(False)


'OK' or 'KO'
False or 'KO'
'False' or 'KO'
0 or 'KO'

'OK' and 'KO'
True and 'KO'
1 and 'KO'

True and 'OK' or 'KO'
True and 'OK' and 'KO'
True and 0 and 'KO'
True and False and 'KO'

True or 'OK' or 'KO'
1 or 'OK' or 'KO'

False and 'OK' or 'KO'
0 and 'OK' or 'KO'

False and 'OK' and 'KO'
False or 'OK' or 'KO'
0 or 'OK' or 'KO'

0 and 0 or 1
0 and (0 or 1)
1 or 0 and 0
(1 or 0) and 0
0 and False or 1
0 and False or True
False and False or True

#%% Modules

import math #
print("The value of pi is", math.pi)

import math as m


from math import pi

#%%

import math
degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)
math.sqrt(2) / 2.0

x = math.sin(degrees / 360.0 * 2 * math.pi)
0.7071067811865476

x = math.exp(math.log(x+1))

# log: e; log10: 10

import math   # This will import math module
print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.72) : ", math.ceil(100.72))


#%% Linear Algebra

import numpy as np 
x = np.array([1,5,2])
y = np.array([7,4,1])
x + y
array([8, 9, 3])
x * y
array([ 7, 20,  2])

#%% Date and time

import datetime 
#today is a function that returns today's date 
print (datetime.date.today())


 
import datetime 
currentDate = datetime.date.today() 
#strftime allows you to specify the date format 
print (currentDate.strftime('%d %b,%Y'))


import datetime 
currentDate = datetime.date.today() 
#strftime allows you to specify the date format 
print (currentDate.strftime
('Please attend our event %A, %B %d in the year %Y'))



import datetime 
currentTime = datetime.datetime.now() 
print (currentTime) 
print (currentTime.hour) 
print (currentTime.minute)
print (currentTime.second)

#%% Conditionals 

x = -10

if x > 0:
    print('x is positive')

#%%
deposit=input("How much would you like to deposit? ")
if deposit > 100 :
     print("You get a free toaster!")
print("Have a nice day")

deposit=input("How much would you like to deposit? ")
if int(deposit) > 100 :
     print("You get a free toaster!")
print("Have a nice day")


deposit=input("How much would you like to deposit? ")
if int(deposit) > 100 :
     print("You get a free toaster!")
print("~End~")


#%% multiple conditions

x = 10000
y = 10

if x < y :
    print('x is less than y')
elif x > 20*y :
    print('x is far greater than y')
elif (x > y and x <= 20*y):
    print('x is far greater than y')   
else:
    print('x and y are equal')

#%% 

""" 

> 90: A
90 >=, > 80: B
80 >=, > 70: C
70 >=, > 60: D
60 >=: You bloody failed
    
"""

grade = float(input('Your grade:'))

if grade > 100:
    
    print ('Are you kidding me?')
    
elif (grade > 90 and grade <= 100):   
    
    print ('You got an A, congrats')
    
    # (94, 100]: A+
    # (92, 94]: A
    # (90, 92]: A-
    
    if (grade > 94 and grade <= 100) :
        
        print('Amazing, an A+')

    elif (grade > 92 and grade <= 94) :
        
        print('Good, an A')        
        
    else:
        
        print('an A-')    
    
    
elif (grade > 80 and grade <= 90):
    
    print ('You got a B, not bad')

elif (grade > 70 and grade <= 80): 
    
    print ('You got a C, work harder')
    
elif (grade > 60 and grade <= 70): 
    
    print ('You got a C, almost a looser')   
    
else: 
    
    print ('You bloody failed, sucker')      
    
#%% Turtle

import turtle 
turtle.forward(100)

# close turtle window:
turtle.Screen().bye()
    
#%%
import turtle
turtle.color('green') 
turtle.forward(100) 
turtle.right(45) 
turtle.color('blue') 
turtle.forward(50) 
turtle.right(45) 
turtle.color('pink') 
turtle.forward(100)
# turtle.Screen().bye()

#%%

import turtle
turtle.forward(100) 
turtle.right(90) 
turtle.forward(100) 
turtle.right(90) 
turtle.forward(100) 
turtle.right(90) 
turtle.forward(100)
    
#%% 

for steps in range(4):
    turtle.forward(100)
    turtle.right(90)


#%%

for steps in range(3):
    turtle.forward(100)
    turtle.right(90)
    
#%%

for steps in range(3):
    turtle.forward(100)
    turtle.right(90)
turtle.color('red')
turtle.forward(200)
    
    
#%%


word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count + 1
print(count)
  
word = 'banana'
count = 0
for letter in word:
    if letter == 'z':
        count = count + 1
print(count)    
    

word = 'bananaZZZZZ'
count = 0
for letter in word:
    if letter == 'Z':
        count = count + 1
print(count) 

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
        print('Done',count)

word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count + 1
        print('Done',count)

word = 'banana'
count = 0
for letter in word:
    if letter == 'n':
        count = count + 1
    print('Done',count)


#%% nested loops
    
    
for steps in range(5):
    turtle.forward(100)
    turtle.right(360/5)
    
    for moresteps in range(5):
        turtle.forward(50)
        turtle.right(360/5)
print ('Done')


#%%

nnn = 16

for steps in range(nnn):
    turtle.forward(100)
    turtle.right(360/nnn)
    
    for moresteps in range(nnn):
        turtle.forward(50)
        turtle.right(360/nnn)
print ('Done')

#%%

for steps in range(4):
    print(steps)


#%%
    
counter=0
while counter<4:
    turtle.forward(100)
    turtle.right(90)
    counter=counter+1
    
    
#%%
    
var = 10                    # Second Example
while var > 0:              
   print ('Current variable value :', var)
   var = var -1

   if var == 5:
       print('KKKK')
       break
   
   print('OK')       
       
print ("Good bye!")


#%% Factorial 

# Python program to find the factorial of a number provided by the user.
# change the value for a different result
num = 500000
# uncomment to take input from the user
#num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
# to be cont’d

elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
       
   print("The factorial of",num,"is",factorial)

