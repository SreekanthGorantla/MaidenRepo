print("Hello, World")

if 5 < 2:
    print("Five is greater than two!")
else:
    print("False.")
    
x = 5
y = "Hello, World!"
print(x)
print(y)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Camel Cas: Each word, except the first, started with a capital letter

myVariableName = "Sree"
print("myVariableName is : " + myVariableName)

#Pascal Case: Each word starts with a capital letter

MyVariableName = "Sree"
print("MyVariableName is : " + MyVariableName)

#Snake Case: Each word is seperated by an underscore character:

my_variable_name = "Sree"
print("my_variable_name is : " + my_variable_name)

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print("x means = " + x)
print("y means = " + y)
print("z means = " + z)

# one value to multiple variables:
x = y = z = "Orange"
print("x is = " + x)
print("y is = " + y)
print("z is = " + z)

#Unpack a collection

fruits = ["Grape", "Mango", "Kiwi"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables

x = "Python is awesome"
print(x)

# output multiple variaples in print() function

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# you can also use the + operator to output multiple variables.

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# for the numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# this will give error
#x = 5
#y = "Sree"
#print(x + y)

x = 5
y = "Sree"
print(x , y)


#Global Variables
# create a valirable outside of a function, and use it inside the function

x = "awesome!"
def myfunc():
    print("Python is " + x)
    
myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

# Create a valirable inside a function, with the same name as the global variable

x = "awesome!"
def myfunc():
    x = "fantastic."
    print("Python is " + x)
    
myfunc()
print("Python is " + x)

# The Global Keyword

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.
#Example: If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "fantastic."
    
myfunc()
print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# to change the value of a global variable inside a function, refer to the variable by using the gloal keyword:

x = "awesome!"
def myfunc():
    global x
    x = "fantastic.!"
    
myfunc()
print("Python is " + x)

# To print data types

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

# ----------------------------------------------------------###
# Python Data Types

# Built-in Data Types
#In programming, data type is an important concept.
#Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:

#Text Type:	str
#Numeric Types:	int, float, complex
#Sequence Types:	list, tuple, range
#Mapping Type:	dict
#Set Types:	set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	NoneType

#Getting the Data type

#you can get the data type of any object by using the type() function:

x = dict(name="John", age=36)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

#Python Numbers

#------------------------------

#There are three numeric types in Python:
#int
#float
#complex
#Variables of numeric types are created when you assign a value to them:

x = 1   # int
y = 2.8 # float
z = 1j  # complex

# To verify the type of any object in Python, use the type() function:
print(type(x))
print(type(y))
print(type(z))

# Int
# Int, or Integer, is a whole number, positive or negative, without decimals, of unlimited length.
# Example
x = 1
y = 23456893243456734
z = -3456782

print(type(x))
print(type(y))
print(type(z))

# Float
# Float or "floating point number" is a number, positive or negative, containing one or more decimals.
#example:
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example:
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
# Complex numbers are written a "j" as the imaginary part:
#Example:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

# Type Conversion#
 # You can convert from one type to another with the int(), float(), complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
 
print(type(a))
print(type(b))
print(type(c))

# Random Number:
# Python does not have a randon() function make a random number, but Puthon has a built-in module called random that can be used to make randon numbers:
# Import the random module, and display a random number between 1 to 9:
import random
print(random.randrange(1, 10))

# Python Casting

#Specify a Variable Type
#There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

#Casting in python is therefore done using constructor functions:

#int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
#float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
#str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
# Int:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Float:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# Strings
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

# Strings
#Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print('Hello')
print("Hello")

# Assign String to a Variable
# Assigning a string to a variable is doen witht he valiable name followed by an equal sign and the string:
a = "Hello"
print(a)

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Strings are Arrays
#Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#However, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to access elements of the string.
# Example: Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

# Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Example: Loop through the letters in the word "banana":
for x in "banana":
    print(x)

#String Leagth
# To get the length if a string, use the len() function.
# Example : The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.
# Example: Check if "free" is present in the following test:
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement

#Example: Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
# Check if NOT
# To check is a certain phrase or character is not present in a string, we can use the keyword not in.
# Example: Check if "epensive" is NOT in the following test:

txt = "The best things in life are free!"
print("expensive" not in txt)

# Use if confidition
# print only if 'expensive' is NOT present.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT prsent.")
    
# Python - Slicing Strings
#Slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
## Example: Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Example: Get the characters from the start to position 5(not included):
b = "Hello, World!"
print(b[:5])

# Slice to the End
# By leaving out the end Index, the range will go to the end.
# get the characters from position 2, and all the way to the end.

b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice fromt he end of the string:
# Example: Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):

b = "Hello, World!"
print(b[-5:-2])

# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# Upper Case
# Example: The Upper() methin returns the string in upper case:
a= "Hello, World!"
print(a.upper())

# Lower Case
# The lower() method returns the string in lower case:
a = "HELLO, WORLD!"
print(a.lower())

# Remove Whitespace
# Whitespace is the sapce before and/or after actual text, and very often you want to remove this space
# Example: The stric() method removes any whitespace from the befinning or the end:

a = "Hello, World!"
print(a.strip())  # returns "Hello, World!"

# Replace String
# Example: The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))

        # Split String
# The split() method returns a list where the test between the specified separator becomes the lsit items.
# Example: The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(","))  # returns ['Hello', 'World!']

# String Methods
# Leans more about String Method with out String Methods Reference
# Python - String Concatenation
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.

# Example: Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# Example: To add space between then, add a " "":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Python - Format - Strings
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
#age = 36
#txt = "My name is Sree, I am " + age
#print(txt)  # Error will come

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them is the string where the placeholders {} are:
# Example: Use the format() method to insert numbers in to strings:

age = 36
txt = "My name is Sree, and I am {}"
print(txt.format(age))
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are paced in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollors for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

