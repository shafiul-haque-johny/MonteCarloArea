import math
import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(1)
N = 10000
hit = 0

report_C = []
report_PI = []

plt.figure(figsize=(6, 6))
plt.plot([-5, 5, 5, -5, -5], [-5, -5, 5, 5, -5], c='Blue')
interval = 1 / 10000

ax = []
ay = []
ag = []
ah = []
ai = []
aj = []

for i in range(0, N+1):
    x = (3 * i * interval)
    y = math.sqrt(9 - (x * x))
    ax.append(x)
    ay.append(y)
plt.plot(ax, ay, c='Red')

for i in range(0, N+1):
    y = -(3 * i * interval)
    x = math.sqrt(9 - (y * y))
    ax.append(x)
    ay.append(y)
plt.plot(ax, ay, c='Red')

for i in range(0, N+1):
    x = -(3 * i * interval)
    y = -math.sqrt(9 - (x * x))
    ag.append(x)
    ah.append(y)
plt.plot(ag, ah, c='Red')
for i in range(0, N+1):
    y = (3 * i * interval)
    x = -math.sqrt(9 - (y * y))
    ag.append(x)
    ah.append(y)
plt.plot(ag, ah, c='Red')

hx = []
hy = []
mx = []
my = []

for i in range(1, N+1):
    x = np.random.uniform(-5, 5)
    y = np.random.uniform(-5, 5)
    if np.sqrt(x ** 2 + y ** 2) < 3:
        hit += 1
        hx.append(x)
        hy.append(y)
    else:
        mx.append(x)
        my.append(y)
    if i in [100, 1000, 10000]:

        # A(square) = 4*r*r = 4*5*5 = 4*25  ; A(circle) = pi*r*r = pi*3*3 = pi*9
        # P(hit) = A(circle)/A(square) => hit/ N = 9*pi / 4*25 => pi = (hit * 4*25) / (N*9)
        report_PI.append((4*25*hit) / (i*9))

plt.scatter(hx, hy, c='Red', s=5)
plt.scatter(mx, my, c='Blue', s=5)

report_C = np.array(report_PI)
report_circle = report_C * 9

print("Value Of PI:")
print(report_PI)

print("Area of Circle:")
print(report_circle)

plt.grid(True, linewidth= 1, linestyle="--")

figure2 = plt.figure(figsize=(6, 6))

plt.xlabel('N(Number of trials)')
plt.ylabel('Estimated PI Value')
plt.title(' Bar Diagrams:Trials vs PI value')

Trials = ['100', '1000', '10000']

# value was taken from simple output because every time it's shows different value
report_PI = [3.4444444444444446, 3.2888888888888888, 3.16]

bar1 = plt.bar(Trials, report_PI)
bar1[0].set_color('Red')
bar1[1].set_color('Green')
bar1[2].set_color('Blue')

figure3 = plt.figure(figsize=(6, 6))

plt.xlabel('N(Number of trials)')
plt.ylabel('Area of the circle')
plt.title(' Bar Diagrams:Trials vs Circle Area')

# value was taken from simple output because every time it's shows different value
report_circle = [31, 29.6, 28.44]

bar2 = plt.bar(Trials, report_circle)
bar2[0].set_color('Red')
bar2[1].set_color('Green')
bar2[2].set_color('Blue')

plt.show()