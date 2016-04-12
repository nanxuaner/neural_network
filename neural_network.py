import numpy as np


def getZ(w, x, b):
    return np.dot(w, x) + b

def perceptron(z):
    if z <= 0:
        return 0
    return 1

def sigmoid(z):
    return 1/(1 + np.exp(-z))
