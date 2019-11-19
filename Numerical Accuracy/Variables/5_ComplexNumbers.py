from cmath import *

# note only those variable initialized with an imaginary part are identified as an object of class complex
a = -3
b = 3.4j
c = 0.0
d = 3 - 5j
e = 4 + 0j
print(isinstance(a, complex))   # prints false
print(isinstance(b, complex))
print(isinstance(c, complex))   # prints false
print(isinstance(d, complex))
print(isinstance(e, complex))

#   Complex Number Operations:
"""
    Complex Numbers include everything you can do with floating point numbers EXCEPT:
    '//', '%' and 'divmod'
"""

#   Built in Stuff:

#   from cmath import *   (library for complex numbered math functions)
#   use of some e.g. functions of cmath library:
x = complex(12.3, 3.4)
y = 5.67+8.9j
print(x, y, x+y, x * y, x/y, cos(x))
print(x * x, pow(x, 2), sqrt(--1))
print(exp(x), pow(e, x))
print(x.real, x.imag, x.conjugate())
print(pow(abs(x), 2), x * x.conjugate())
