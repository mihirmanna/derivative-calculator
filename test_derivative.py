import unittest
from derivative import *


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.poly_eqn = Function(FunTyp.POLY, 3, 8)
        self.exp_eqn = Function(FunTyp.EXP, 2, 5)
        self.log_eqn = Function(FunTyp.LOG, 1, 6)
        self.sin_eqn = Function(FunTyp.SIN, 7)
        self.cos_eqn = Function(FunTyp.COS, 9)
        self.nested_eqn = Function(FunTyp.POLY, 1, 2, [
            Function(FunTyp.POLY, 1, 1, [
                Function(FunTyp.SIN, 1, inside=[
                    Function(FunTyp.POLY, 5, 1),
                    Function(FunTyp.POLY, 1, 0)
                ])
            ])
        ])
        self.product_eqn = Function(FunTyp.POLY, 1, 1, [
            Function(FunTyp.SIN, 1),
            Function(FunTyp.EXP, 1, 8)
        ], True)

    def test_polynomial(self):
        self.assertEqual(str(self.poly_eqn), '3x^8')

    def test_exponential(self):
        self.assertEqual(str(self.exp_eqn), '2*5^x')

    def test_logarithm(self):
        self.assertEqual(str(self.log_eqn), 'log_6(x)')
    
    def test_sine(self):
        self.assertEqual(str(self.sin_eqn), '7sin(x)')
    
    def test_cosine(self):
        self.assertEqual(str(self.cos_eqn), '9cos(x)')

    def test_nested(self):
        self.assertEqual(str(self.nested_eqn), '((sin(5x+1)))^2')

    def test_product(self):
        self.assertEqual(str(self.product_eqn), '(sin(x)*8^x)')


class TestDerivativeRules(unittest.TestCase):
    def setUp(self):
        self.poly_eqn = Function(FunTyp.POLY, 8, 3)
        self.sin_eqn = Function(FunTyp.SIN, 5)
        self.cos_eqn = Function(FunTyp.COS, 4)
        self.exp_eqn = Function(FunTyp.EXP, 9, 2)
        self.log_eqn = Function(FunTyp.LOG, 7, 6)

    def test_power_rule(self):
        power_rule(self.poly_eqn)
        self.assertEqual(self.poly_eqn.a, 24)
        self.assertEqual(self.poly_eqn.b, 2)

    def test_sine_rule(self):
        sine_rule(self.sin_eqn)
        self.assertEqual(self.sin_eqn.type, FunTyp.COS)
        self.assertEqual(self.sin_eqn.a, 5)

    def test_cosine_rule(self):
        cosine_rule(self.cos_eqn)
        self.assertEqual(self.cos_eqn.type, FunTyp.SIN)
        self.assertEqual(self.cos_eqn.a, -4)

    def test_exponent_rule(self):
        exponent_rule(self.exp_eqn)
        self.assertEqual(self.exp_eqn.a, 9*log(2))

    def test_logarithm_rule(self):
        logarithm_rule(self.log_eqn)
        self.assertEqual(self.log_eqn.type, FunTyp.POLY)
        self.assertEqual(self.log_eqn.a, 7/log(6))
        self.assertEqual(self.log_eqn.b, -1)


if __name__ == '__main__':
    unittest.main()
    