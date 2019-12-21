from matplotlib.pyplot import plot, show
from numpy.ma import arange

ti = 0
tf = 100
dt = 0.001
N = 2000
tau = 5
listN = [N]
listT = [ti]

for t in arange(ti + dt, tf, dt):
    N = N - N/tau * dt
    listN.append(N)
    listT.append(t)

plot(listT, listN)
show()
