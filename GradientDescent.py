import random

import numpy as np

from InertiaStrategies import RandomInertiaEvolutionaryStrategy
from ObjectiveFunctions import gradient_rastgirin
from PSO import f_rosenbrock




def gradient_descent_op(iterations, gradient_function, alpha=0.1, initial_random_guess=10):
    position = [
        random.uniform(-initial_random_guess, initial_random_guess),
        random.uniform(-initial_random_guess, initial_random_guess),
    ]
    MAX_GRADIENT = 100
    positions = [position]

    for i in range(iterations):
        gradient = gradient_function(position)
        if abs(gradient[0]) > MAX_GRADIENT:
            gradient[0] = MAX_GRADIENT * 1 if gradient[0] > 0 else -1
        if abs(gradient[1]) > MAX_GRADIENT:
            gradient[1] = MAX_GRADIENT * 1 if gradient[1] > 0 else -1

        position[0] = position[0] - alpha * gradient[0]
        position[1] = position[1] - alpha * gradient[1]
        positions.append(position)

    print("gradient descent")
    print(position, f_rosenbrock(position))
    return positions


gradient_descent_op(1000, gradient_function=gradient_rastgirin)
