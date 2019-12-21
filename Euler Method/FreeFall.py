from matplotlib.pyplot import plot, show

t = 0
dt = 0.001
v = 0
x = 100
g = -9.8
listX = [x]
listV = [v]
listT = [t]

while(1):
    v = v + g * dt
    x = x + v * dt
    t = t + dt
    if x < 0:
        break
    listX.append(x)
    listV.append(v)
    listT.append(t)

plot(listT, listV, 'b')
plot(listT, listX, 'g')

show()
