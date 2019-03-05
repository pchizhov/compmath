import math


def f(x):
    return 0.5 * math.exp(- x ** 2) + x * math.cos(x)


def df(x):
    return - x * math.exp(- x ** 2) + math.cos(x) - x * math.sin(x)


def ddf(x):
    return - math.exp(- x ** 2) + 2 * (x ** 2) * math.exp(- x ** 2) - 2 * math.sin(x) - x * math.cos(x)


A = -1
B = 1
X0 = 0.5
INTERSECTION = (B - A) * (- f(A)) / (f(B) - f(A)) + A
EPSILON = 0.0000001


def newton(x, num):
    new_x = x - (f(x)/df(x))
    while new_x > B or new_x < A:
        new_x = (x + new_x) / 2
    if abs(new_x - x) < EPSILON:
        return new_x, num
    return newton(new_x, num + 1)


def chords(x, num):
    new_x = x - (f(x) * (x - INTERSECTION)) / (f(x) - f(INTERSECTION))
    if abs(new_x - x) < EPSILON:
        return new_x, num
    return chords(new_x, num + 1)


if __name__ == "__main__":
    if f(X0) * ddf(X0) < 0:
        print("Solved with the Newton's method:")
        newton_solution = newton(X0, 0)
        print(f'x = {newton_solution[0]}, iterations_num = {newton_solution[1]}')
    print("Solved with the method of chords:")
    chords_solution = chords(X0, 0)
    print(f'x = {chords_solution[0]}, iterations_num = {chords_solution[1]}')
