import math
import Libreria_computacion_cuantica as op
import unittest
class prueba_funciones_con_complejos(unittest.TestCase):

    def prueba_suma (test):
        suma = op.suma_cplx((6,9),(3,-2))
        test.assertAlmostEqual(suma[0],9)
        test.assertAlmostEqual(suma[1],7)
        
    def prueba_resta(test):
        resta = op.resta_cplx((1,-6),(2,8))
        test.assertAlmostEqual(resta[0],2)
        self.assertAlmostEqual(resta[1],-14)

    def prueba_producto(test):
        producto = op.multplx((5,-4),(3,-3))
        test.assertAlmostEqual(producto[0],2)
        self.assertAlmostEqual(producto[1],-27)

    def prueba_division(test):
        division = op.divplx((2,-4),(4,-2))
        test.assertAlmostEqual(division[0],0.8)
        test.assertAlmostEqual(division[1],-0.6)

    def prueba_modulo(test):
        modulo = op.modul_cplx((7, 2))
        test.assertAlmostEqual(modulo, 7,2)


    def prueba_conjugado(test):
        conjugado = op.conjugado_cplx((2, 7))
        test.assertAlmostEqual(conjugado[0], 2)
        test.assertAlmostEqual(conjugado[1], -7)

    def prueba_polar(test):
        polar = op.polar_cplx((4, 3))
        tes.assertAlmostEqual(polar[0], 4*(2**(1/2)))
        tes.assertAlmostEqual(polar[1], 0.7853981633974483)

    def prueba_fase_complejo(tes):
        suma = op.fase_cplx((3, 3))
        test.assertAlmostEqual(suma, (1/4)*math.pi)
