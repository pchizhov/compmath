import math
from matplotlib import mlab
import pylab

A = 1
B = 2
Y = 1


def f(x, y):
    return (x * y * y - y) / x


def euler(n):
    dist = (B - A) / n
    x = [A + dist * i for i in range(n)]
    y = [0 for _ in range(n)]
    y[0] = Y
    for k in range(n - 1):
        y[k + 1] = y[k] + f(x[k], y[k]) * dist
    return x, y


def runge_kutta(n):
    _, y_pred = euler(n)
    dist = (B - A) / n
    x = [A + dist * i for i in range(n)]
    y = [0 for _ in range(n)]
    y[0] = Y
    for k in range(n - 1):
        # y[k + 1] = y[k] + f(x[k], y[k]) * dist / 2 + f(x[k + 1], y_pred[k + 1])
        y[k + 1] = y[k] + dist * f(x[k] + dist / 2, y[k] + dist / 2 * f(x[k], y[k]))
    return x, y


def plot(x, y):
    pylab.scatter(x, y)
    pylab.plot(x, y)
    pylab.show()


if __name__ == "__main__":
    x_list, y_list = euler(10)
    plot(x_list, y_list)
    print(x_list, y_list)
    x_list, y_list = runge_kutta(10)
    plot(x_list, y_list)
    print(x_list, y_list)