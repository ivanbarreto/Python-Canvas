import unittest
from canvaspep8 import *


class TddCanvas(unittest.TestCase):

    def test_matrix_is_created(self):
        result = [[0, 0, 0], [0, 0, 0]]
        teste = Canvas(3, 2)
        equal = False
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_clear_canvas(self):
        source = [[2, 2, 2], [2, 2, 2]]
        teste = Canvas(3, 2)
        equal = False
        teste.matrix = source
        teste.clearcanvas()
        result = [[0, 0, 0], [0, 0, 0]]
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_color_pixel(self):
        result = [[0, 2, 0], [0, 0, 0]]
        teste = Canvas(3, 2)
        equal = False
        teste.colorpixel(2, 1, 2)
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_vertical_segment(self):
        result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 'W', 0, 0, 0], [
            0, 'W', 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        teste = Canvas(5, 6)
        equal = False
        teste.verticalsegment(2, 3, 4, 'W')
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_horizontal_segment(self):
        result = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                  [0, 0, 'W', 'W', 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        teste = Canvas(5, 6)
        equal = False
        teste.horizontalsegment(3, 4, 4, 'W')
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_rectangle(self):
        result = [[0, 0, 0, 0, 0], [0, 0, 'W', 'W', 0], [0, 0, 'W', 'W', 0], [
            0, 0, 'W', 'W', 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        teste = Canvas(5, 6)
        equal = False
        teste.rectangle(3, 2, 4, 4, 'W')
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)

    def test_floodfill(self):
        result = [['J', 'J', 'J', 'J', 'J'], ['J', 'J', 'Z', 'Z', 'J'], [
            'J', 'W', 'J', 'J', 'J'], ['J', 'W', 'J', 'J', 'J'], [
                'J', 'J', 'J', 'J', 'J'], ['J', 'J', 'J', 'J', 'J']]
        teste = Canvas(5, 6)
        equal = False
        teste.matrix = [[0, 0, 0, 0, 0], [0, 0, 'Z', 'Z', 0], [
            0, 'W', 0, 0, 0], [0, 'W', 0, 0, 0], [0, 0, 0, 0, 0], [
                0, 0, 0, 0, 0]]
        teste.floodfill(2, 2, 'J')
        if result == teste.matrix:
            equal = True
        self.assertTrue(equal)


if __name__ == '__main__':
    unittest.main()
