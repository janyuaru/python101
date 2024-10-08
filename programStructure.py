import matplotlib.pyplot as plt
import math

n = 300 #data point
if n < 10:
    n = 10
x = []
y = []
for k in range(n):
    x.append(k*16*math.pi/n)
    y.append(0.1*k*math.sin(x[k]))
plt.plot(x, y)
plt.show()
