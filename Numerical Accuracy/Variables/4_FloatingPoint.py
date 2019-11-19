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
    note: - if width is too small, the minimum necessary width to print the certain floating point number is used
          - if precision is set to 0, the output is 
"""

x = 100.0/7.0

# note the difference in representation of %f and %e when width is not specified
print('%.3f %.5e' % (x, x))

# specified widths and precisions
print('%10.5f %20.3e' % (x, x))

# if width is too small, the minimum necessary width to print the certain floating point number is used (%7.3e case)
print('%7.3f %7.3e' % (x, x))

# a precision of 0 prints in integer form
print('%.0f %.0e' % (x, x))

# if you're actually reading this repository to learn python, I leave you to think on the following case :P
# see where the rounded off numbers start going wrong and think WhY?

print('%.30f %.30f %.30f %.30f' % (8.1, 1e-12, 1e-15, 1e-17))
# letting x = a tuple
x = (1.234567890125, 1.23456789012501)
print('%.20f %.20f' % x)
print(x[0], x[1])   # x[i] is the (i+1)th element of tuple
print('%.11f %.11f' % x)
print(x)

# the %d descriptor:
x = 12345.6
y = -x
print('%.0f %.0f' % (x, y))  # rounds off to whole number
print('%d %d' % (x, y))   # truncates floating decimal
