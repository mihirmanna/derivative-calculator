import unittest
from derivative import *


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.poly_eqn = Function(FunTyp.POLY, 3, 8)
        self.exp_eqn = Function(FunTyp.EXP, 2)
        self.log_eqn = Function(FunTyp.LOG, 6)
        self.sin_eqn = Function(FunTyp.SIN)
        self.cos_eqn = Function(FunTyp.COS)
        self.nested_eqn = Function(FunTyp.POLY, 1, 2, [
            Function(FunTyp.SIN, inside=[
                Function(FunTyp.POLY, 5, 1),
                Function(FunTyp.POLY, 1, 0)
            ])
        ])

    def test_polynomial(self):
        self.assertEqual(str(self.poly_eqn), '3x^8')

    def test_exponential(self):
        self.assertEqual(str(self.exp_eqn), '2^x')

    def test_logarithm(self):
        self.assertEqual(str(self.log_eqn), 'log_6(x)')
    
    def test_sine(self):
        self.assertEqual(str(self.sin_eqn), 'sin(x)')
    
    def test_cosine(self):
        self.assertEqual(str(self.cos_eqn), 'cos(x)')

    def test_nested(self):
        self.assertEqual(str(self.nested_eqn), '(sin(5x+x^0))^2')


if __name__ == '__main__':
    unittest.main()
    