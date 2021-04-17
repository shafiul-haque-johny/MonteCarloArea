import math
import random
import numpy as np
import matplotlib.pyplot as plt

# plt.plot([0, 1], [0, 1], color='Blue')
# plt.plot([4, 3], [0, 1], color='Blue')

rectangle = plt.Rectangle((0, 0), 4, 2, fc='none', ec="Blue")
plt.gca().add_patch(rectangle)

plt.xlim(left=-0.2, right=4.2)
plt.ylim(bottom=-0.2, top=2.2)

N = 1000
hit = 0
miss = 0
report_hit = []
report_PI = []
report_C = []
ax = []
ay = []
interval = 1 / 100

"""
for i in range(1, N+1):
    x = (i * interval)
    y = math.sqrt(1 - (x * x))
    ax.append(x)
    ay.append(y)
plt.plot(ax, ay, c='Red')
"""

for i in range(1, N+1):
    x = random.uniform(0, 1)
    y = random.uniform(0, 2)
    if y <= x:
        hit += 1
        plt.scatter(x, y, c='Green')
    else:
        plt.scatter(x, y, c='Red')

    x = random.uniform(3, 4)
    y = random.uniform(0, 2)
    if y <= 4 - x:
        hit += 1
        plt.scatter(x, y, c='Green')
    else:
        plt.scatter(x, y, c='Red')

    x = random.uniform(1, 3)
    y = random.uniform(0, 1)
    plt.scatter(x, y, c='Green')

    x = random.uniform(1, 3)
    y = random.uniform(1, 2)
    if np.sqrt((x-2) ** 2 + (y-1) ** 2) < 1:
        hit += 1
        plt.scatter(x, y, c='Green')
        if i in [100, 1000, 10000]:
            report_PI.append((2 * hit) / i)
        else:
            pass
    else:
        plt.scatter(x, y, c='Red')

    if i in [100, 1000, 10000]:
        report_hit.append(hit)
    else:
        pass


report_C = np.array(report_PI)
report_circle = report_C * 2

print("Half Circle Area:")
print(report_circle)


print("Total Hits:")
print(report_hit)

plt.show()