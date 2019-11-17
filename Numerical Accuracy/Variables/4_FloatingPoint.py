a = 3.4
b = 3
c = 3e-3
d = -3E-2
e = 30.
f = .56
g = float(3)
print(isinstance(a, float))
print(isinstance(b, float))     # prints false
print(isinstance(c, float))
print(isinstance(d, float))
print(isinstance(e, float))
print(isinstance(f, float))
print(a, ' ', c, ' ', d, ' ', e, ' ', f, ' ', g, ' are floating point numbers')

#   Floating point Operations
"""
    Floating point operations include everything you can do with integers
    note: '/' is a floating-point division ~ and that's why I converted 4/x to int in line 20 on Integers.py
    further note: use of '/' results in a float number
                  use of '//', '%', 'divmod' results in integer quotient but the result is still a float format
"""
x = 5.01
y = 7//x + 6/x - 3**x + 12.3 % x
# y = 1.0 + 1.1976.. - 245.6843.. + 2.0, note: ** is used to for 'raised to power' when floating numbers are involved
print(y)

#   Built in Functions
x = abs(-3.5)
print(x)
x = float(6)
print(x)
x = divmod(4.5, 2.5)
print(x)
x = pow(1.25, 10)
print(x)

#   Formatted Outputs:
"""
    %<width>.<precision>f      (fixed-point form)
    %<width>.<precision>e      (scientific form)
"""

#   in process of completing this file, ZzzZZzzZZzZzzzz
