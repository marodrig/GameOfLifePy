import unittest

from src.cell import Cell
from src.display_cells import DisplayCells


class TestDisplayCells(unittest.TestCase):
    def setUp(self):
        self.board = DisplayCells()
        self.expected_matrix = [['.' for _ in range(4)] for _ in range(4)]

    def tearDown(self):
        self.board = None

    def test_4x4_matrix_of_dead_cells(self):
        self.board.init_board(4, 4)
        self.assertListEqual(self.expected_matrix, self.board.display_board())

    def test_one_cell_in_a_4x4_matrix(self):
        self.expected_matrix[0][1] = '*'
        self.board.init_board(4, 4)
        self.board.game.add_cell(Cell(0, 1))
        self.assertListEqual(self.expected_matrix, self.board.display_board())

    def test_cell_with_two_neighbours_lives_in_next_iteration(self):
        self.expected_matrix[0][1] = '*'
        self.board.init_board(4, 4)
        self.board.game.add_cell(Cell(0, 0))
        self.board.game.add_cell(Cell(0, 1))
        self.board.game.add_cell(Cell(0, 2))

        self.board.game.get_next_iteration()
        self.assertListEqual(self.expected_matrix, self.board.display_board())
