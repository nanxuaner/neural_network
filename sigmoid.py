import numpy

def getZ(w, x):
    return numpy.dot (w, x)

def sigmoid(z):
    return 1/(1 + numpy.exp(-z))