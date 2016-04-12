import numpy
def getZ (w, x):
    return numpy.dot (w, x)

def perceptron(z):
    if z <= 0:
        return 0
    return 1
