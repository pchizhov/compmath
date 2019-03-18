from matplotlib import mlab
import pylab


ARRAY_X = [0.083, 0.472, 1.347, 2.117, 2.947]
ARRAY_Y = [-2.132, -2.013, -1.613, -0.842, 2.973]


def plot(func):
    x_min = ARRAY_X[0]
    x_max = ARRAY_X[-1]
    dx = 0.001
    x_list = mlab.frange(x_min, x_max, dx)
    y_list = [func(arg) for arg in x_list]
    pylab.plot(x_list, y_list)
    pylab.show()


def lagrange_polynomial(x):
    ln = 0
    for i in range(len(ARRAY_X)):
        ln += p(x, i) * ARRAY_Y[i]
    return ln


def p(x, i):
    polynomial = 1
    for j in range(len(ARRAY_X)):
        if j != i:
            polynomial *= (x - ARRAY_X[j]) / (ARRAY_X[i] - ARRAY_X[j])
    return polynomial


def spline(x):
    i = 0
    while x > ARRAY_X[i]:
        i += 1
    return (x - ARRAY_X[i - 1]) * (ARRAY_Y[i] - ARRAY_Y[i - 1]) / (ARRAY_X[i] - ARRAY_X[i - 1]) + ARRAY_Y[i - 1]


if __name__ == "__main__":
    plot(lagrange_polynomial)
    plot(spline)
