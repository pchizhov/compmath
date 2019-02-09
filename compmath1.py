EPSILON = 0.001


def solve_with_gauss(a, b):
    for i in range(len(a)):
        divisor = a[i][i]
        a[i][i:len(a)] = [a[i][j] / divisor for j in range(i, len(a))]
        b[i] /= divisor
        if i == len(a):
            break
        for j in range(i + 1, len(a)):
            difference = a[j][i]
            a[j] = [a[j][k] - difference * a[i][k] for k in range(len(a))]
            b[j] -= difference * b[i]
    x = [0 for _ in range(len(a))]
    for i in reversed(range(len(a))):
        x[i] = b[i] - sum(x[j] * a[i][j] for j in range(i + 1, len(a)))
    return x


def solve_with_jacobi(a, b):
    matrix = [[- a[i][j] / a[i][i] for j in range(len(a))] for i in range(len(a))]
    remainder = [b[i] / a[i][i] for i in range(len(a))]
    return jacobi_iterate(matrix, remainder, remainder)


def jacobi_iterate(m, r, x):
    new_x = [sum(m[i][j] * x[j] for j in range(len(m)) if j != i) + r[i] for i in range(len(m))]
    if max(abs(x[i] - new_x[i]) for i in range(len(x))) < EPSILON:
        return new_x
    return jacobi_iterate(m, r, new_x)


if __name__ == "__main__":
    left_part = [[4.003, 0.207, 0.519, 0.281],
                 [0.416, 3.273, 0.326, 0.375],
                 [0.297, 0.351, 2.997, 0.429],
                 [0.412, 0.194, 0.215, 3.628]]
    right_part = [0.425, 0.021, 0.213, 0.946]
    gauss_result = solve_with_gauss(left_part, right_part)
    print("System solution with Gauss method:")
    for n in range(len(gauss_result)):
        print("x" + str(n + 1), "=", gauss_result[n])
    jacobi_result = solve_with_jacobi(left_part, right_part)
    print("System solution with Jacobi method:")
    for n in range(len(jacobi_result)):
        print("x" + str(n + 1), "=", jacobi_result[n])
