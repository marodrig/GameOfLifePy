import unittest

from src.game_of_life import GameOfLife
from src.game_of_life import Cell


class GameOfLifeShould(unittest.TestCase):

    def setup(self):
        self.game = GameOfLife()
        pass

    def one_cell_has_no_neighbours(self):
        cell = Cell(0,0)
        self.game.addCell(cell)
        self.assertEqual(0, len(self.game.getNeighbours(cell)))