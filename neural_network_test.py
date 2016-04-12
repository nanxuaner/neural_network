import unittest

class NeuralNetworkTest(unittest.TestCase):
    def setUp(self):
        print "setup"

    def tearDown(self):
        print "teardown"

    def test_getZ(self):
        print "getZ"

    def test_perceptron(self):
        print "perceptron"

    def test_sigmoid(self):
        print "sigmoid"

if __name__ == '__main__':
    testSuite = unittest.TestLoader().loadTestsFromTestCase(NeuralNetworkTest)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
