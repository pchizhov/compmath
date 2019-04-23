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
    dist = (B - A) / n
    x = [A + dist * i for i in range(n)]
    y = [0 for _ in range(n)]
    y[0] = Y
    for k in range(n - 1):
        y_p = y[k] + f(x[k], y[k]) * dist
        y[k + 1] = y[k] + (f(x[k], y[k]) + f(x[k + 1], y_p)) * dist / 2
    return x, y


def plot(x1, y1, x2, y2):
    pylab.scatter(x1, y1)
    pylab.plot(x1, y1)
    pylab.scatter(x2, y2)
    pylab.plot(x2, y2)
    pylab.show()


if __name__ == "__main__":
    x_list1, y_list1 = euler(10)
    x_list2, y_list2 = runge_kutta(10)
    plot(x_list1, y_list1, x_list2, y_list2)
