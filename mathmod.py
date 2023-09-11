import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

g = 9.81
x0 = int(input("x0: "))
x_t = x0
x_buff = x0
Vxy = float(input("V0xy: "))

x = np.array([0,16,30,46,74,100,150,190,226,240,280])
y = np.array([160,152,138,106,84,40,4,21,55,60,148])
f =  interpolate.interp1d(x, y, kind = 3)
x1 = np.arange(0,280,1)
plt.ion()
for t in np.arange(0, 3, 0.01):
    plt.clf()
    plt.xlabel('х(mm)')
    plt.ylabel('у(mm)')
    plt.plot(x1, f(x1), '-')
    dx = -(f(x1)[x_t+1]-f(x1)[x_t-1])/2
    cosa = np.sqrt(1/(dx*dx+1))
    Vy = Vxy*dx*cosa + g
    if dx > 0 and Vy < 0:
        Vy = Vxy*dx*cosa + g*2
    if x_t == 278 or 0:
        Vxy = -Vy/(dx*cosa)
    else:
        Vxy = Vy/(dx*cosa)
    Vx = Vxy*cosa
    x_buff = x_buff + Vx*0.01
    x_t = int(round(x_buff))
    print(Vxy, Vx, Vy, dx, cosa, x_t, f(x1)[x_t])
    plt.plot(x_t, f(x1)[x_t], "o")
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.01)
plt.ioff()
plt.show()
