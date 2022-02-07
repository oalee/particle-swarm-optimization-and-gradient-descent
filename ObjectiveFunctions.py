import numpy as np


def f(x):
    # simple function
    return 2 * x[0] ** 2 - 8 * x[0] + 1


def f_rosenbrock(x):
    a = 0
    b = 1
    return (a - x[0]) ** 2 + b * (x[1] - x[0] ** 2) ** 2


def gradient_rosenbroch(x):
    a = 0
    b = 1
    dx1 = -2 * (a - x[0]) + b * -4 * x[0] * (x[1] - (x[0] ** 2))
    dx2 = 2 * b * (x[1] - (x[0] ** 2))
    return np.array(dx1, dx2)


def f_rastrigin(x):
    value = (
            (x[0] ** 2 - 10 * np.cos(2 * np.pi * x[0]))
            + (x[1] ** 2 - 10 * np.cos(2 * np.pi * x[1]))
            + 20
    )
    return value


def gradient_rastgirin(x):
    dx1 = 2 * x[0] + 20 * np.pi * np.sin(2 * np.pi * x[0])
    dx2 = 2 * x[1] + 20 * np.pi * np.sin(2 * np.pi * x[1])
    return np.array(dx1, dx2)
