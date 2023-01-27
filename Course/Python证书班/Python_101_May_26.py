# -*- coding: utf-8 -*-
"""
Created on Sat May 26 10:30:53 2018

@author: James
"""

print('Hickory Dickory Dock! The mouse ran up the clock')
print("Hickory Dickory Dock! The mouse ran up the clock") 
# how to use print
print("It's a beautiful day in the neighborhood") 
print('It's a beautiful day in the neighborhood') 
print('Hickory Dickory Dock!\nThe mouse ran up the clock') 
print("""Hickory Dickory Dock! 
The mouse ran up the clock""")

print('''Hickory Dickory Dock!
The mouse ran up the clock''')



#%% Introduction to Data Types


str_eg = 'this is a string'
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
# 'a', key; 'apple', value; key-value pair

vowels = {'a', 'e', 'i' , 'o', 'u'} #set, no order no duplicate

print(str_eg)
print(fruits)
print(numbers)
print(alphabets)
print(vowels)


#%% type function

a = 5
print(a, "is of type", type(a))
a = 2.0
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

type(2/1) # wtf, float
type(1+2)
type(2*1)
type(5/2)
type(2/1+1) # wtf, float
type(2/1*1) 

#%% Integers

0b111 # binary
1*2**0 + 1*2**1 + 1*2**2
# **, exponent 

0B10011001 # binary

0o12345 #octal
5*8**0 + 4*8**1 + 3*8**2 + 2*8**3 + 1*8**4

0XAA 
10*16**0 + 10*16**1
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 (A), 11 (B), 12 (C), 13 (D), 14, (E), 15(F)

0XFFF
15*16**0 + 15*16**1 +15*16**2

#%% Decimal

(1.1 + 2.2) == 3.3

#%% Boolean

x = (1 == True) # True and False are both case-sensitive
True == 1 # output: True
True is 1 # output: False
True + 1 # output: 2

y = (1 == False)
False == 0 # output: True
False is 0 # output: False
False + 1 # output: 1
type(False) # output: bool, Boolean
type (False + True) # output: integer
type ((False + True) is 1)
type ((False + True) == 1)

a = True + 4
b = False + 10
print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


type('apple')
apple  = 1
type (apple)

apple  = ['apple']
type (apple)

apple  = ['apple']
type (apple [0])
type(apple[0][0])

apple  = ['apple', 4, 'orange', True]
type (apple [1])

apple  = ('apple', 4, 'orange', True, '1.0', 1.0)
type (apple)
type (apple[2])
type (apple[4])
type (apple[5])


apple  = ('apple', (4,), 'orange', True, '1.0', 1.0)
apple[1]


#%% Data conversion

>>> print(3.14, int(3.14))
>>> print(3.9999, int(3.9999))   # NO ROUNDING    
# This doesn't round to the closest int!

print(3.0, int(3.0))
print(-3.999, int(-3.999))        
# Note that the result is closer to zero
print("-3.999", int("-3.999")) 
print("2345", int("2345"))   
# parse a string to produce an int
str_eg = '2345'
type(str_eg)
# 123'+'456'

str_eg_convt = int(str_eg)
type(str_eg_convt)


print(float("123"))
print(type(float("123")))

# float(True)

print(str(17))
print(str(123.45))
print(type(str(17)))
print(type(str(123.45)))

#%% Implicit data conversion

num_int = 123
num_flo = 1.23
num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))
print(num_int+num_str)

#%% Variables 

message = "What's up, Doc?"
n = 17
pi = 3.14159
print(message)
print(n)
print(pi)

message = 'Sup'

day = "Thursday"
print(day)
day = "Friday"
print(day)
day = 21
print(day)

firstName = 'James'
print(firstname)

first_name # preferred

#%% User input

name = input("What is your name? ")  
print(name) 

a = input('First number')
b = input('Second number')
c = a + b
print(c)


a = input('First number')
b = input('Second number')
c = int(a) + float(b)
print(c)


a = int(input('First number'))
b = int(input('Second number'))
c = a + b
print(c)

first_Name = input("What is your first name? ")
last_Name = input("What is your last name? " )
print("Hello " + first_Name + " " + last_Name) 


a = 5
print('The value of a is', a)
# Output: The value of a is 5


print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

print(1,2,3,4,sep='@@',end='~end~')


#%% Strings

>>> fruit = 'banana'
>>> letter1 = fruit[1]
>>> letter1
>>> letter2 = fruit[0]
>>> letter2

>>> fruit = 'banana ice cream'
>>> len(fruit)
# elements in strings are not mutable

>>> first = 'boy'
>>> second = 'friend'
>>> first + second
>>> (first + second)*4


>>> first = '123'
>>> second = '456'
>>> first + second
>>> (first + second)*4

str_eg = 'Hello, James'
'H' in str_eg
'h' in str_eg

#%% Slicing

>>> fruit = 'banana'
>>> fruit[:3] # right side, not included
>>> fruit[3:] # left side, included
>>> fruit[3:3] # empty

# 0  1  2  3  4  5
# b  a  n  a  n  a
#-6 -5 -4  -3 -2 -1

>>> fruit[:]
>>> fruit[-1]
>>> fruit[-2]
>>> fruit[:-2]
>>> fruit[-2:]

>>> fruit[:2] + fruit[2:]
>>> fruit[:9] + fruit[9:]
# fruit[9], error
# fruit[9:], no error

>>> fruit[0:5:2]
fruit[0:5:-2] # 0:5, direction defined
>>> fruit[1:5:2]
>>> fruit[0:5:3]

fruit[::-1]

#%% Formatting

print ("My name is %s and weight is %d kg!" % ('Zara', 21))

nBananas = 27
"We have %d bananas." % nBananas

nBananas = 27
"We have %6d bananas." % nBananas

nBananas = 27
"We have %8d bananas." % nBananas

caseCount = 42
caseContents = "peaches"
print ("We have %d cases of %s today." % (caseCount, caseContents))


'%s' % 'soup' # default: aligned right
'%6s' % 'soup'
'%-10s' % 'soup' # aligned left
'%10s' % 'soup' # aligned left

"%d" % 1107
"%5d" % 1107
'%30d' % 1107
'%2d' % 1107
'%5d' % 505
'%-5d' % 505
'%05d'%42  # default: space; 0
'%5d' % (10/3)
'%05d' % (10/3)
'%5d' % (20/3) # no rounding
'%05d' % (20/3) # no rounding
'%.0f' % (20/3) # rounding


"%f" % 0.0 # default: 6 digits (decimal point)
"%f" % 1.5
pi = 3.141592653589793
"%f" % pi  # rounding
"%.0f" % pi
"%.15f" % pi
"%.6f" % pi # rounding
"%5.1f" % pi # decimal point takes one space
"%5.3f" % pi # rounding
"%-7.1f" % pi
"%-7.0f" % pi

#%% Formatter

print("Sammy has {} balloons.".format(5))

"Hi {0}, balance is {1:9.3f}".format('James', 123.45678)
# 0, index 0
# 1, index 1
# 9, 9 digits (decimal point included)
#.3, three digits after decimal point

'{0} + {1}'.format('James','Laverna')
'{1} + {0}'.format('James','Laverna')

print("Sammy ate {0:f} percent of a {1}!".format(75.12345678, "pizza")) #default: 6 digits

print("Sammy ate {0:.2f} percent of a {1}!".format(75.12345678, "pizza"))

print("Sammy ate {0:10.2f} percent of a {1}!".format(75.12345678, "pizza"))

print("Sammy ate {0:.4f} percent of a {1}!".format(75.12345678, "pizza"))

print("Sammy ate {0:.5f} percent of a {1}!".format(75.12345678, "pizza"))

print("Sammy ate {0:.0f} percent of a {1}!".format(75.12345678, "pizza"))


print("Sammy ate {0:10.4f} percent of a {1}!".format(75.12345678, "pizza"))

print("Sammy ate {0:20.0f} percent of a {1}!".format(75.12345678, "pizza"))
# allotted a minimum of 20 places including the "."

print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))

print("Sammy has {0:2} red {1:10}!".format(5, "balloons"))

print("Sammy has {0:1} red {1:20}!".format(5, "balloons"))


print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

print("Sammy has {0:^4} red {1:>16}!".format(5, "balloons"))

print("Sammy has {0:*<4} red {1:@^16}!".format(5, "balloons"))

print("Sammy has {0:$^4} red {1:!>16}!".format(5, "balloons"))


for i in range(3,13):
    print(i, i*i, i*i*i)
    
    # aligned left by default

for i in range(3,13):
    print("{:3d} {:4d} {:5d}".format(i, i*i, i*i*i))

for i in range(3,13):
    print("{:6d} {:6d} {:6d}".format(i, i*i, i*i*i))

for i in range(3,13):
    print("{:^6d} {:^6d} {:^6d}".format(i, i*i, i*i*i))

for i in range(3,13):
    print("{:<6d} {:<6d} {:<6d}".format(i, i*i, i*i*i))






