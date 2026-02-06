import unittest
from calculadora import sumar, restar, multiplicar

class PruebasCalculadora(unittest.TestCase):

  def test_suma(self):
    self.assertEqual(sumar(2,3), 5)

  def test_resta(self):
    self.assertEqual(resta(10,5), 5)

  def test_multiplicacion(self):
    self.assertEqual(multiplicar(3,3), 9)

if __name__ == '__main__':
  unittest.main()
