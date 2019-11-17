#   dividing with zero exception
try:
    print("Let's calculate x/y :P")
    x = input('Enter x: ')
    y = input('Enter y: (enter 0 :3)')
    z = x / y  # exception thrown on this line if y == 0
    print(z)
except:
    print('you cannot divide with zero')

#   Integer Operations:
"""
    playing with '+', '-', '*', '/' operators while learning how the value returned by the expression on the right side 
    of the assignment operator '=' is assigned to the left hand side
"""
x = 3
print(x)
x = int(x + 6 - 2*x)
print(x)
y = int(4/x)                 # because I want x and y to be integers
print(y)
#   the remainder operator '%'
x = -2
y = -5 % x
print(y)                     # note that the remainder is of the same sign as of the divisor x

#   Built in Functions:
x = abs(-3)                  # absolute (positive) value
print(x)
x = int(4.56)                # type conversion to int
print(x)
x = divmod(-5, 3)            # divmod(a, b) => (a/b, a%b)    note: the output is a tuple
print(x)
x = pow(3, 6)                # pow(a, b) => 3^6 or 3**6

#   Formatted Output:
"""
    %d or %<width>d
    note: if width is too small, the minimum necessary width to print the certain integer is used
    e.g. printing 12345678 in width 3 (as portrayed in code ahead) results in 12345678 to take its minimum required
    amount of width i.e. 8 to be printed
"""
print('%d %d' % (123, 12345678))
print('%7d %3d' % (123, 12345678))
