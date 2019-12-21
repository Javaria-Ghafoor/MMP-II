from math import *

# example function
def func(x):
    return (x**3)*exp(-x)


def Simpson(f, a, b, n):  # Simpson Rule
    if n % 2 == 0:
        n += 1     # to ensure that n is odd
    h = (b-a)/(n-1)      # no. of intervals = n - 1
    s1 = s2 = 0
    for i in range(3, n-1, 2):
        s1 += f(a+(i-1)*h)
    for i in range(2, n, 2):
        s2 += f(a+(i-1)*h)
    return (h/3)*(f(a)+4*s2+2*s1+f(b))


a = 0       # lower limit of integral
b = 1       # upper limit of integral
n = 200
print('i=', Simpson(func, a, b, n))
