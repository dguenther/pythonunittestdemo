class Cell:
    def __init__(self, living):
        self.living = living

    def __repr__(self):
        return '@' if self.living else 'x'