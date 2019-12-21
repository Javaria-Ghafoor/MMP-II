from math import exp

# two example functions
def func1(x):
    return (x**3)*exp(-x)


def func2(x):       # argument x not being ued in body of this function
    return 3


def Trapz(f, a, b, n):       # trapezoidal rule
    h = (b-a)/(n-1)     # no. of trapezoids = n - 1
    I = (1/2)*(f(a)+f(b))*h    # initialize I
    for i in range(2, n):
        I += f(a+(i - 1)*h)*h      # I = I + func(a+j*h), keep updating I, j = i - 1
    return I


a = 0    # lower limit of integral
b = 1    # upper limit of integral
n = 200  
print('Integral of func1(x)=', Trapz(func1, a, b, n))
print('Integral of func2(x)=', Trapz(func2, a, b, n))
