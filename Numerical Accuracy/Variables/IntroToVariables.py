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
print(a, ' belongs to ', type(a))
print(b, ' belongs to ', type(b))
print(c, ' belongs to ', type(c))
print(d, ' belongs to ', type(d))
#   use of isinstance() function
print(c, 'is a complex number?: ', isinstance(c, complex))
print(d, 'is a complex number?: ', isinstance(d, complex))
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
#   inputting variables.. Python 3.7 uses input() while Python 2.7 uses raw_input()
"""
    Note that one can enter any data type here as an input to 'p', the statement 'Enter an integer' does not bound the
    user from entering some string or floating number etc. The same goes for 'q' and 'r'
"""
p = input('Enter an integer: ')
q = input('Enter a floating point number: ')
r = input('Enter a complex number: ')
print('p = ', p)
print('q = ', q)
print('r = ', r)
