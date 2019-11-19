from math import e

# no.1
x = 0.001
y = (1.0+x)-1.0
print(x, y, x == y)
print('%.16f %.16f' % (x, y))

# no.2
x = 0.001
y = (1.1*x)*1.0
print(x, y, x == y)
print('%.16f %.16f' % (x, y))

# no.3
x = 1.0/6.0
y = x+x+x+x+x+x
print(y, y == 1.0)
print('%.18f %.18f' % (x, y))

# no.4
# from math import e
x = e/11.0
y = 1.0/x
z = 1.0/y
print(x == z)
print('%.18f %.18f %.18f' % (x, y, z))

# no.5
x = 1.0e-20
y = 5.0e-324
print(1.0+x == 1.0, y/2.0)
print('%.6e %.6e' % (x, y))

# no.6
a = 0.75+1.0e-16
b = 0.75
c = 0.5
d = 0.5-1.0e-16
print(a > b, c > d, a+c > b+d)
print('%.16f %.16f %.16f %.16f' % (a, b, c, d))
print('%.16f %.16f' % (a+c, b+d))
