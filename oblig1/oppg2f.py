import matplotlib.pylab as plt
import numpy as np

n = 1000
x = np.linspace(-2, 2, n)
rho = 1.0/5

X = np.zeros(n)
Y = np.zeros(n)
mx = np.zeros(n)
my = np.zeros(n)
nx = np.zeros(n)
ny = np.zeros(n)
rx = np.zeros(n)
ry = np.zeros(n)

def sigma(x):
    return 0.25 * (2 * x * (np.sqrt(4 * x**2 + 1)) + np.arcsinh(2*x))

for i in range(n):
    nx[i] = (2*x[i]/np.sqrt(4*x[i]**2 + 1))
    ny[i] = (-1/np.sqrt(4*x[i]**2 + 1))

    X[i] = x[i] + rho*(-2*x[i])/(np.sqrt(4*x[i]**2 + 1))
    Y[i] = x[i]**2 + rho/np.sqrt(4*x[i]**2 + 1)

    mx[i] = rho*(np.cos(sigma(x[i])/rho)*2*x[i] + np.sin(sigma(x[i])/rho)*-1)/np.sqrt(4*x[i]**2 + 1)
    my[i] = rho*(-np.sin(sigma(x[i])/rho)*2*x[i] + np.cos(sigma(x[i])/rho)*-1)/np.sqrt(4*x[i]**2 + 1)

    rx[i] = mx[i] + X[i]
    ry[i] = my[i] + Y[i]

plt.plot(x, x**2, "g-")
plt.plot(X, Y, "b-")
plt.plot(rx, ry, "r")
plt.legend(["s(x)", "(X(x), Y(x))", "r(x)"])
plt.savefig("oppg_f.png")
plt.show()
