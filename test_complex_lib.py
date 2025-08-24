import unittest
import math
import Complex_lib as cl

class TestComplexLib(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(cl.suma((2,3),(1,1)), (3,4))
        self.assertEqual(cl.suma((0,0),(5,-2)), (5,-2))

    def test_resta(self):
        self.assertEqual(cl.resta((2,3),(1,1)), (1,2))
        self.assertEqual(cl.resta((0,0),(5,-2)), (-5,2))

    def test_producto(self):
        self.assertEqual(cl.producto((1,2),(3,4)), (-5,10))
        self.assertEqual(cl.producto((0,1),(0,1)), (-1,0))

    def test_division(self):
        self.assertEqual(cl.division((1,2),(3,4)), (0.44, 0.08))
        self.assertAlmostEqual(cl.division((1,2),(3,4))[0], 0.44, places=2)
        self.assertAlmostEqual(cl.division((1,2),(3,4))[1], 0.08, places=2)

    def test_modulo(self):
        self.assertEqual(cl.modulo((3,4)), 5.0)
        self.assertEqual(cl.modulo((0,0)), 0.0)

    def test_conjugado(self):
        self.assertEqual(cl.conjugado((3,4)), (3,-4))
        self.assertEqual(cl.conjugado((5,-7)), (5,7))

    def test_cartesiano_a_polar(self):
        r, theta = cl.cartesiano_a_polar((1,1))
        self.assertAlmostEqual(r, math.sqrt(2), places=5)
        self.assertAlmostEqual(theta, math.pi/4, places=5)

    def test_polar_a_cartesiano(self):
        z = cl.polar_a_cartesiano((2, math.pi/2))
        self.assertAlmostEqual(c[0], 0.0, places=5)
        self.assertAlmostEqual(c[1], 2.0, places=5)

    def test_fase(self):
        self.assertAlmostEqual(cl.fase((1,1)), math.pi/4, places=5)
        self.assertAlmostEqual(cl.fase((-1,0)), math.pi, places=5)

if __name__ == '__main__':
    unittest.main()
