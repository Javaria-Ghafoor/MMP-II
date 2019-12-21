
from math import exp

# two example functions
def func1(x):
    return (x**3)*exp(-x)


def func2(x):       # argument x not being ued in body of this function
    return 3


def LeftPoint(f, a, b, n):       # left point riemann sum
    h = (b-a)/n     # no. of trapezoids = n
    I = 0    # initialize I
    for i in range(0, n):
        I += f(a+i*h)*h
    return I

def RightPoint(f, a, b, n):     # right point riemann sum
    h = (b-a)/n
    I = 0
    for i in range(0, n):
        I += f(a+(i+1)*h)*h
    return I

def MidPoint(f, a, b, n):
    h = (b-a)/n
    I = 0
    for i in range(0, n):
        I += f(a+(i-1/2)*h)*h
    return I


a = 0    # lower limit of integral
b = 1    # upper limit of integral
n = 200

print(LeftPoint(func1, a, b, n))
print(LeftPoint(func2, a, b, n))
print(RightPoint(func1, a, b, n))
print(RightPoint(func2, a, b, n))
print(MidPoint(func1, a, b, n))
print(MidPoint(func2, a, b, n))
