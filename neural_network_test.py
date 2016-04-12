import unittest
import neural_network
import numpy as np

class NeuralNetworkTest(unittest.TestCase):
    def setUp(self):
        self.w = [1, 1]
        self.x = [1, 1]
        self.b = 2
        print "setup"


    def tearDown(self):
        print "teardown"

    def test_getZ(self):
        self.assertEqual(neural_network.getZ(self.w, self.x, self.b), 4)
        print "getZ"

    def test_perceptron(self):
        z = neural_network.getZ(self.w, self.x, self.b)
        self.assertEqual(neural_network.perceptron(z), 1)
        print "perceptron"

    def test_sigmoid(self):
        z = neural_network.getZ(self.w, self.x, self.b)
        self.assertEqual(neural_network.sigmoid(z), (1/(1 + np.exp(-4))))
        print "sigmoid"

if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(NeuralNetworkTest)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
