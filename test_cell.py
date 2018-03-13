import unittest
from cell import Cell

class CellTestCase(unittest.TestCase):
    def test_constructor(self):
        cell = Cell(True)
        self.assertTrue(cell.living)
    
    def test_repr(self):
        cell = Cell(True)
        self.assertEqual('@', repr(cell))
        cell.living = False
        self.assertEqual('x', repr(cell))


if __name__ == '__main__':
    unittest.main()