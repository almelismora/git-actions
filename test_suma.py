import unittest
from suma import sumar, restar, multiplicar, dividir

class TestSumar(unittest.TestCase):

    def test_sumar(self):

        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

class TestRestar(unittest.TestCase):

    def test_restar(self):

        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-10, 5), -15)
        self.assertEqual(restar(-10, -5), -5)

class TestMultiplicar(unittest.TestCase):

    def test_multiplicar(self):

        self.assertEqual(multiplicar(3, 3), 9)
        self.assertEqual(multiplicar(-3, 3), -9)
        self.assertEqual(multiplicar(-3, -3), 9)

class TestDividir(unittest.TestCase):

    def test_dividir(self):

        self.assertEqual(dividir(4, 2), 2.0)
        self.assertEqual(dividir(-4, 2), -2.0)
        self.assertEqual(dividir(-4, -2), 2.0)
        
        with self.assertRaises(ZeroDivisionError):
           dividir(4, 0)


if __name__ == '__main__':
    unittest.main()