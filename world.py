from cell import Cell
import random

class World:
    def __init__(self, cols, rows):
        self.cells = [
            [
                Cell(bool(random.getrandbits(1))) for _ in range(cols)
            ] for _ in range(rows)
        ]

    def __repr__(self):
        output = ''
        for row in self.cells:
            for cell in row:
                output += str(cell)
            output += '\n'
        return output

    @property
    def rows(self):
        return len(self.cells)

    @property
    def cols(self):
        if len(self.cells) > 0:
            return len(self.cells[0])
        return 0