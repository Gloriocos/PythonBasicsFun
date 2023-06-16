# COMMENTS
# this is a one line comment

"""
this is
a multi
line comment
"""
import csv
import math

# GETTING INPUT FROM THE USER
print("Enter a number:")
num = input() # num is a variable
# what type is num?
print(type(num))
print("The number doubled is :",2*num)

# we need to convert num from a string
# to a integer
num_int=int(num)
print("The number doubled is :",2*num_int)

# CONDITIONALS (IF STATEMENTS)
# if some condition is true
# then execute some code
x=10
if x ==5:
    print("x is 5")
elif x==7:
    print("x is 7")
else:
    print("x is not 5 and x is not 7")

# LOOPS
# use a loop when you want to repeat code
#we have for loops and while loops in python
# for item in sequence:
#     body of for loop (code you want repeated)
for character in "python":
    print(character)

# we can also make our own sequences
# with range(start,stop,step)
for i in range(0 , 5, 1):
    print(i)
for i in range(5):
    print(i)
for i in range(0,5):
    print(i)
# task:write a for loop to print
# the first 20 even numbers
# 2,4,...,38,40
for i in range(2,42,2):
    print(i,end=" ")
print()
# while loops
# while condition is true:
#   body of loop(code to be repeated)
#   progress towards the condition
#       being false
# let's re-whrite our for loop
# with a while loop
i=2
while i<=40:
        print(i,end=" ")
        i+=2 #progress
# note that conditionals and loops
# con be bested inside each other
# juest pay attention to the indentation

# FUNCTIONS
# a named sequence of statements
# we have been using pre-defined
# functions
# print(), int(), input(), range(), ...
# now, we define our own functions
# def function_name(parameter list):
#   body of function (code to run
#       when function is "called")
# functions don't run until they are
# called

# example #l
# function whith no inputs and no
# returnn
def say_Hello():
    print("hello")

# we need to call the function
# for it to tun
for i in range(10):
    say_Hello() #call

# example #2
# function with one input and no
# return
def say(message):
    print(message)

say("hi!!")
say("how are you??")
say("goodbye...")

# example #3
# function with one input
# and one return (output)
def compute_circle_area(radius):
    area =3.14 * radius ** 2
    return area # send back to
    # calling code

result = compute_circle_area(5)
print("result:",result)

# LISTS
# a list is a sequence of items
# declare a list using []
# and a comma separated list of values
# each item in a list is at a
# unique index (starts at 0)
#           -4 -3 -2 -1
#            0  1  2  3
list_ints =[10, 4, -2, 9]
print(list_ints)
print(list_ints[1], list_ints[-3])
#
list_ints[0]=4000
print(list_ints)
#
list_ints[-1]="hello"
print(list_ints)
#
print(len(list_ints))
#
list_ints.append(42)
print(len(list_ints))

empty_list=[]
print(len(empty_list))
# we can have a list of lists
# called a nested list
# or a 2-dimensional (2D) list
nested_list=[[0,1],[2,3],[],[8]]
print(nested_list)
print(nested_list[1])
print(nested_list[1][1])

# looping through list items
cities=["hangzhou","beijing","shanghai"]
for city in cities:
    print(city)
print()
# task:try writing the above for loop
# using a while loop
i=0
while i<len(cities):
    print("i:",i,"cities[i]:",cities[i])
    i+=1
# common list operators
print(cities)
# list concatenation
# adding 2 lists togther
cities += ["shenzhen","chongqing"]
print(cities)
# list repetition
# repeating items in a list
repeated_list =3 * ["guangzhou","tianjin"]
print(repeated_list)
# list slicing :
# get some items from a list
print(cities[1:])
# start index:stop index
# start index is included
# start index is not included
print(cities[:2])
print(cities[2:])
#
cities_copy=cities[:]
print("copy:",cities_copy)
cities_copy[0]="HANGZHOU"
#
print("copy:",cities_copy)
print("original:",cities)
# some list methods (functions that
# operate on an object)
# append() add item to end of list
cities.append("new york city")
print(cities)
# remove() delete item based on value
cities.remove("shanghai")
print(cities)
# pop() delete item based on index
cities.pop(-1)
print(cities)

#
#
string_list=["new","york","city"]
#
one_string="".join(string_list)
print(one_string)
# create a list from a string
comma_separated_value_string="new,york,city"
#
#
sl2=comma_separated_value_string.split(",")
print(sl2)
#
star_separated_value_string="new***york***city"
sl3=star_separated_value_string.split("***")
print(sl3)
# FILES
# a file stores data on your file system
# example:main.py is a file string
# python program memory

# .csv file extension stands for
# comma separated value

# 3 step file processing template
# 1.open the file (for reading or writing)
# 2.process the file (read or write)
# 3. close the file
filename="data.csv"  #data.csv must
# be in same folder as main.py for this
# to work
# 1. open the file for reading
infile=open(filename,"r") #"r" is mode
# for reading
#
#
#
reader = csv.reader(infile)
table=[]
for row in reader:
    print(row)
    table.append(row)
#
infile.close()

print("after closing file,table:")
print(table) # nested list (2D list)

header=table.pop(0)
print("header:",header)
print("table:")
print(table)
