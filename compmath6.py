import math

A = 1
B = 2

def f(x):
    return math.sqrt(x + 1) * math.log10(x + 1)


def int_f(x):
     return 2 * ((x + 1) ** (3 / 2)) * (3 * math.log(x + 1) - 2) / (9 * math.log(10))


def newton_leibnitz():
    return int_f(B) - int_f(A)


def split(h):
    n = int((B - A) / h)
    x = [A + i * h for i in range(n)]
    return x, [f(i) for i in x], n


def trapezium(h):
    x, y, n = split(h)
    return h * sum((y[i + 1] + y[i]) / 2 for i in range(n - 1))


def simpson(h):
    x, y, n = split(h)
    n -= 1
    n //= 2
    return 2 * h / 3 * (y[0] + y[2 * n] + sum(2 * y[2 * i + 1] for i in range(n)) + sum(y[2 * i] for i in range(1, n)))


if __name__ == "__main__":
    print("Solved with Newton-Leibnitz method:", newton_leibnitz())
    print("Solved with trapezium method:", trapezium(0.000001))
    print("Solved with Simpson's method:", simpson(0.000001))
