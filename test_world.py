import unittest
from world import World
from cell import Cell

class WorldTestCase(unittest.TestCase):
    def test_constructor(self):
        world = World(4, 1)
        self.assertEqual(1, len(world.cells))
        self.assertEqual(4, len(world.cells[0]))

    def test_rows(self):
        world = World(1, 4)
        self.assertEqual(4, world.rows)

    def test_cols(self):
        world = World(2, 4)
        self.assertEqual(2, world.cols)

    def test_string(self):
        world = World(1, 1)
        alive = Cell(True)
        dead = Cell(False)
        world.cells = [[alive, dead], [dead, alive]]
        self.assertEqual(str(world), f'{alive}{dead}\n{dead}{alive}\n')

if __name__ == '__main__':
    unittest.main()