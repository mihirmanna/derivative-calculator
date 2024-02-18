import unittest
from derivative import *


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.func1 = Function(FunTyp.POLY, 3, 8)
        self.func2 = Function(FunTyp.EXP, 2, 7)
        self.func3 = Function(FunTyp.LOG, 6, 5)
        self.func4 = Function(FunTyp.SIN, 10, 4)  # b argument is unused
        self.func5 = Function(FunTyp.COS, 9, 1)  # b argument is unused

    def test_polynomial(self):
        self.assertEqual(str(self.func1), '3(x)^8')

    def test_exponential(self):
        self.assertEqual(str(self.func2), '2*7^(x)')

    def test_logarithm(self):
        self.assertEqual(str(self.func3), '6log_5(x)')
    
    def test_sine(self):
        self.assertEqual(str(self.func4), '10sin(x)')
    
    def test_cosine(self):
        self.assertEqual(str(self.func5), '9cos(x)')


if __name__ == '__main__':
    unittest.main()
    