"""
    We can use the type() function to know which class a variable or a value belongs to
    and the isinstance() function to check if an object belongs to a particular class.
"""
#   In python, you can declare/initialize a variable without mentioning its data type
a = 4        # int
b = 2.0      # float
c = 2 + 7j   # complex
d = 'hello'  # str
#   use of type() function
print (a, ' belongs to ', type(a))
print (b, ' belongs to ', type(b))
print (c, ' belongs to ', type(c))
print (d, ' belongs to ', type(d))
#   use of isinstance() function
print (c, 'is a complex number?: ', isinstance(c, complex))
print (d, 'is a complex number?: ', isinstance(d, complex))
"""
    Now, since int, float, complex etc are inbuilt classes, therefore they have an
    inbuilt constructor.
    in python:
    to construct an instance of a certain class class_name (say) you do the following:
    object = class_name()
"""
#   how we declare a certain data type in python
x = int()       # an object of class int() gets created on execution of this line
y = float()
z = complex()
#   inputting variables.. Python 3.7 uses input() while Pyhton2.7 uses raw_input()
x = input('Enter an integer: ')
y = input('Enter a floating point number: ')
z = input('Enter a complex number: ')
print ('x = ', x)
print ('y = ', y)
print ('z = ', z)
