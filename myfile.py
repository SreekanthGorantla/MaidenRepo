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
