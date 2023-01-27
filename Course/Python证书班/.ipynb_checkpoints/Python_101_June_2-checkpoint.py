# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 10:25:08 2018

@author: James
"""

# %% String Methods

str = "       ";
print(str.isspace())
str = "      A";
print(str.isspace())


str = "123456"  # Only digit in this string
print(str.isdigit())
str = " 123456ABC"
print(str.isdigit())

# %% Work on Letters

message = 'Hello World'
print(message.lower())
print(message.upper())
print(message.swapcase())

message = 'Hello World'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
# It returns a copy of the string
# with only its first character capitalized.
print(message.replace('Hello', 'Hi'))


str = "this is a string example....wow!!!"
print(str.capitalize())

print('this is an example'.capitalize())

str = "this is string example....wow!!!"
print(str.title())


str = "this is string example....wow!!! this is really string"
print(str.replace("is", "was"))
print(str.replace("is", "was", 2))
print(str.replace("is", "was", 3))


ss = "bananas are always good"
print(ss.count("a"))
print(ss.count("s"))
print(ss.count("q"))
print(ss.find("m"))
# check to see where the first “m” occurs in the string ss

# %%

count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
        print(count)
print(count, 'letter(s) o(s) found')


count = 0
for letter in 'Hello World':
    print(count)
    if(letter == 'o'):
        count += 1  # count = count + 1
print(count, 'letter(s) o(s) found')


count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
    print(count)
print(count, 'letter(s) o(s) found')

count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
print(count)
print(count, 'letter(s) o(s) found')

# %%

count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
print(count)
print('-the end-')


count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
    print(count)
print('-the end-')

count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1
print('-the end-')
print(count)

count = 0

# This is a for loop

for letter in 'Hello World':

    # This is an if

    if(letter == 'o'):
        count += 1  # count = count + 1

print('-the end-')


count = 0
for letter in 'Hello World':
    if(letter == 'o'):
        count += 1  # count = count + 1

# %%

# empty list
my_list = []

# list of integers
my_list = [1, 2, 3]

# list with mixed datatypes
my_list = [1, "Hello", 3.4]


number_list = [10, 20, 30, 40]
number_list[0]
number_list[1]
number_list[1:]
number_list[1:2]
number_list[1:3]
number_list[::2]
number_list[1::2]

guests = ['Christopher', 'Susan', 'Bill', 'Satya']

# print the last entry in the list
print(guests[-1])

# print the second last entry in the list
print(guests[-2])

[1, 2, 3]
[1, 2, 3]
[1, 2,      3]
[1,    2, 3]

[1, 2, 3] == [1, 2, 3]
[1, 2, 3] is [1, 2, 3]
a = [1, 2, 3]
b = [1, 2, 3]
a == b  # true
a is b  # false

a = [1,    2, 3]
b = [1, 2, 3]
a == b  # true
a is b

a = [1,    2, 3]
c = a  # true
a is c

'1,2,3'
'1,2, 3'
'1, 2,      3'
'1,    2, 3'

# %%

a = [1, 'hi', 1.0, True]
b = [1, 'hi', 1.0,      True]
c = a
a[1]
b[1]
c[1]

a[1] = 2
a[1]
b[1]
c[1]

temp = a
x = temp
x = x*2  # create a new address


e = "1, 'hi', 1.0, True"
f = "1, 'hi', 1.0,      True"

# %% index()

guests = ['Christopher', 'Susan', 'Bill', 'Satya']
guests = ['Christopher', 'Susan', 'Bill', 'Satya', 'Bill', 'Bill']

# this will return the index in the list
# where the name Bill is found
print(guests.index('Bill'))  # Find only the first
aList = [123, 'xyz', 'zara', 'abc']
print("Index for xyz : ", aList.index('xyz'))
print("Index for zara : ", aList.index('zara'))


names = ['Chris', 'James']
ages = [18, 16]
weights = [150, 170]

James_index = names.index('James')
print('Hi', names[James_index], ': your age is ', ages[James_index])


# %%

list1, list2 = [123, 'xyz', 'zara', 'abc'], [456, 700, 200]
print("min value element : ", min(list1))  # error
print("min value element : ", min(list2))

# %% Nested list

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_list[1][1]

my_list[2][2]

my_list = [[[0, 0, 1], 2, 3], [4, 5, 6], [7, 8, 9]]


my_list[0][0][1]

# %% append()

guests = ['Christopher', 'Susan', 'Bill', 'Satya']

# add a new value to the end of the list
guests.append('Steve')

# display the last value in the list
print(guests[-1])

# %% pop()

t = ['a', 'b', 'c']
x = t.pop(1)
t

# %%

t = ['a', 'b', 'c']
del t[1]

# %%

t = ['a', 'b', 'c']
t.remove('b')


guests = ['Christopher', 'Susan', 'Bill', 'Satya']

# add a new value to the end of the list
guests.remove('Christopher')

# display the last value in the list
print(guests[0])

# %%

guests = []
name = "  "
while name.upper() != "DONE":
          name = input("Enter guest name (enter DONE if no more names) : ")
         if name.upper() != "DONE" :
                    guests.append(name)
guests.sort()
for guest in guests :
         print(guest)

# %% Add, extend

t1 = ['a', 'b', 'c']  # recommended over +
t2 = ['d', 'e']
t1.extend(t2)
t1

# %% join
t = ['bananas', 'are', 'good', 'for', 'you']
delimiter = ' '
s = delimiter.join(t)


# %% insert

aList = [123, 'xyz', 'zara', 'abc']
aList.insert(3, 2009)
print("Final List : ", aList)

# %% split

s = 'Eat more bananas, will u?'
t = s.split()


s = 'bananas-are-good-for-you'
delimiter = '-'
t = s.split(delimiter)

array_num = '18_16_15'
delimiter = '_'
t = array_num.split(delimiter)


# %% Aliasing

a = ['1', 1,1.0]

temp = a

temp = []

# a unchanged, temp []

a = ['1', 1,1.0]

temp = a

temp [1] = True  # a, temp, same object


a = ['1', 1,1.0]

temp = a

temp = temp*2

# from aliasing to cloning


a = ['1', 1,1.0]

temp = a[:]  # cloning

temp [1] = True  # a, temp, same object

# %%

guests = ['Christopher', 'Susan','Bill','Satya'] 

# Find out how many entries are in the list
nbrEntries = len(guests)

# Create a loop that executes once for each entry
for steps in range(nbrEntries) :
         print(guests[steps])

# range, a must


pow2 = [2 ** x for x in range(10)]
# Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(pow2)


pow2 = [2 ** x for x in range(10) if x > 5]
pow2
[64, 128, 256, 512]
odd = [x for x in range(20) if x % 2 == 1]
odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
[x+y for x in ['Python ', 'C '] for y in ['Language','Programming']]
['Python Language', 'Python Programming', 'C Language', 'C Programming']


even = [x for x in range(20) if x % 2 == 0]

even = [[x for x in range(20) if x % 2 == 0]]

even = [x for x in range(20) if (x % 2 == 0 or x % 3 == 0)]

even = [x for x in range(20) if (x % 2 == 0 and x % 3 == 0)]

# %% tranpose

matrix = [[1, 2], [3,4],[5,6],[7,8]] # nested list
print(matrix)
transpose = [[row[i] for row in matrix] for i in range(2)]
print(transpose)

matrix = [[1, 2], [3,4],[5,6],[7,8]] 
row_num = len(matrix[0])
# nested list
print(matrix)
transpose = [[row[i] for row in matrix] for i in range(row_num)]
print(transpose)

# %% intro to dictionary

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

# %% dict

# using dict()
dict_eg = {1: 'apple', 2:'ball'}

dict_eg = {}
dict_eg['A'] = 'apple'
dict_eg['B'] = 'ball'

dict_eg = dict({1: 'apple', 2:'ball'})

type(my_dict)
# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2,'ball')])
type(my_dict)

dict_eg = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict['Name']: ", dict_eg['Name'])
print("dict['Age']: ", dict_eg['Age'])

# %%

dict_eg = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_eg)
dict_eg['School'] = "DPS School" # Add new entry
print(dict_eg)
print("dict['School']: ", dict_eg['School'])

# %% modify key-value pair

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
inventory['pears'] = 0

# %%

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict['Name'] # remove entry with key 'Name’
print(dict)
dict.clear()     # remove all entries in dict
print(dict)
del dict        # delete entire dictionary


is
isinstance

'1' in [1, 2]

1.0 in [1, 2]


# %% dictionary methods


inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}


print(inventory.get("apples"))
print(inventory.get("cherries"))  # output: None
print(inventory.get("cherries", 0))  # Default value, overwrite
print(inventory.get("apples", 0))
print(inventory.get("cherries"))

# %% Update

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female'}
dict.update(dict2)
print ("Value : %s" % dict)

# %%

dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" % dict.setdefault('Age', None)) # overwritten
print ("Value : %s" % dict.setdefault('Sex', None))

# %%

dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" % dict.keys())

# %%

dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" % dict.items())

# %%

dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" % dict.values())

# %% # del: clear variable

dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = dict1.copy()
print("New Dictionary : %s" % str(dict2))

# %% in: membership of keys

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares)
# Output: True
print(2 not in squares)
# membership tests for key only not value
# Output: False
print(49 in squares)

# %%

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:  # key at each iteration stored in i
    print(squares[i])  # extract value only


# %%

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[1]['age']

people = {'A': {'name': 'John', 'age': '27', 'sex': 'Male'},
          'B': {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people['B']['sex']


# %%


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
people[3] = {}
people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'
print(people[3])

# %%

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'}}

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])

people.keys()

people.values()

people.items()

people[3].keys()


# %%


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'},
          3: {'name': 'Luna', 'age': '24', 'sex': 'Female', 'married': 'No'},
          4: {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}}
del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])


# %%

people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():

    # wrong: for p_id, p_info in people.keys()

    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])

# %%

nested_eg = [[1, 2],[3,4]]

for i in range(2):

    print(nested_eg[i])

    for j in range(2):

        print(nested_eg[i][j])


# %% Tuple
tup1 = (50);

tup1 = (50,)

# only parentheses is not enough
my_tuple = ("hello")
print(type(my_tuple))  # Output: <class 'str'>

my_tuple = ("hello",)


# %%

tup = ('physics', 'chemistry', 1997, 2000)
print (tup)
del tup
print ("After deleting tup : ")
print (tup)

del tup[1]  # error, unsupported

# %% Set

# initialize my_set
my_set = {1, 3}
print(my_set)
# if you uncomment line 9,
my_set[0]  # you will get an error, no index for set
# add an element
my_set.add(2)  # Output: {1, 2, 3}
print(my_set)

my_set = {1, 3.0, True, 'True',False}
my_set = {3.0, True, 1, 'True',False} # ==

my_set = {1, 3.0, True, 'True',False,0}

my_set = {1}

my_set = {1, 1.0} # no discrimination, 1 == 1.0 (True)

my_set = {1, 3.0, True, 'True',False} 

my_set = {1, 3.0, True, 'True',0, False} 

our_set = {1, '1', False}

our_set.add (True)  # ==

our_set.add (0)


my_set.add(frozenset([2, 3,4]))
print(my_set)

# %%


# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)


my_set.remove(6)
print(my_set)

# %% set operations

A = {1, 2, 3, 4, 5};

B = {4, 5, 6, 7, 8}
# use | operator; Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)


# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
A - B
B - A

A & B
