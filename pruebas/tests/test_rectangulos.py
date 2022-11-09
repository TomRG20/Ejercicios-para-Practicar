import unittest

from pruebasPoligonales.rectangulos import areaRectangulo


# clase de prueba de rectangulos que hereda de testcase
class TestRectangulos(unittest.TestCase):

    # nuestro primer test
    def test_area_rectangulos(self):
        base = 2
        altura = 4

        area = areaRectangulo(base = base, altura = altura)

        self.assertEqual(area, 8)


if __name__ == '__main__':
    unittest.main()
