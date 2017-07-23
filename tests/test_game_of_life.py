import unittest

from src.game_of_life import Cell
from src.game_of_life import GameOfLife


class GameOfLifeTest(unittest.TestCase):
    def setUp(self):
        self.game = GameOfLife()

    def tearDown(self):
        self.game = None

    def test_one_cell_has_no_neighbours(self):
        cell = Cell(0, 0)
        self.game.add_cell(cell)
        self.assertEqual(0, len(self.game.get_neighbours(cell)))

    def test_two_adjacent_cells_are_neighbours(self):
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 1)
        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.assertEqual(1, len(self.game.get_neighbours(cell_one)))

    def test_two_far_away_cells_are_not_neighbours(self):
        cell_one = Cell(0, 1)
        cell_two = Cell(0, 20)
        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.assertEqual(0, len(self.game.get_neighbours(cell_one)))

    def test_cell_in_middle_of_3x3_matrix_should_have_eight_neighbours(self):
        self.create_3x3_matrix()
        self.assertEqual(8, len(self.game.get_neighbours(Cell(1, 1))))

    def create_3x3_matrix(self):
        for i in range(3):
            for j in range(3):
                cell = Cell(i, j)
                self.game.add_cell(cell)

    def test_one_lonely_cell_dies_in_next_iteration(self):
        cell = Cell(0, 0)
        self.game.add_cell(cell)
        self.game.get_next_iteration()
        self.assertFalse(cell.get_is_alive())


if __name__ == '__main__':
    unittest.main()
