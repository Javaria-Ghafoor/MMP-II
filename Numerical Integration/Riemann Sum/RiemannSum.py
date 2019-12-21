import numpy as np

import matplotlib.pyplot as plt


def f(x): return 1/(1+x**2)


a = 0
b = 5
N = 10      # no of rectangles

x = np.linspace(a, b, N+1)  # start:a (included), end:b (included), num:N+1 (no. of equally spaced numbers)

y = f(x)    # since x is an array, y also becomes an array

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(x, y, 'b')
x_left = x[:-1]     # Left endpoints
y_left = y[:-1]
plt.plot(x_left, y_left, 'b.', markersize=10)
plt.bar(x_left, y_left, width=(b-a)/N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Left Riemann Sum, N = {}'.format(N))

plt.subplot(1, 3, 2)
plt.plot(x, y, 'b')
plt.subplot(1, 3, 2)
plt.plot(x, y, 'b')
x_mid = (x[:-1] + x[1:])/2 # Midpoints
y_mid = f(x_mid)
plt.plot(x_mid, y_mid, 'b.', markersize=10)
plt.bar(x_mid, y_mid, width=(b-a)/N, alpha=0.2, edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

plt.subplot(1, 3, 3)
plt.plot(x, y, 'b')
x_right = x[1:]     # Left endpoints
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right, y_right, width=-(b-a)/N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))

plt.show()

dx = (b-a)/N
x_left = np.linspace(a, b-dx, N)
x_midpoint = np.linspace(a + dx/2, b - dx/2, N)
x_right = np.linspace(a + dx, b, N)

# print
print("Partition with", N, "subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:", left_riemann_sum)
midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:", midpoint_riemann_sum)
right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:", right_riemann_sum)

# exact solution
I = np.arctan(b) - np.arctan(a)
print(I)

# error
print("Left Riemann Sum Error:", np.abs(left_riemann_sum - I))
print("Midpoint Riemann Sum Error:", np.abs(midpoint_riemann_sum - I))
print("Right Riemann Sum Error:", np.abs(right_riemann_sum - I))
