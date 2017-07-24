import unittest

from src.game_of_life import Cell
from src.game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):
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

    def test_cell_with_two_neighbours_lives_in_next_iteration(self):
        survivor_cell = Cell(0, 1)
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 2)

        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.game.add_cell(survivor_cell)

        self.game.get_next_iteration()

        self.assertTrue(survivor_cell.get_is_alive())

    def test_cell_with_one_neighbour_dies(self):
        survivor_cell = Cell(0, 1)
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 2)

        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.game.add_cell(survivor_cell)

        self.game.get_next_iteration()

        self.assertFalse(cell_two.get_is_alive())

    def test_cell_with_more_than_three_neighbours_dies(self):
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 1)
        cell_three = Cell(0, 2)
        cell_four = Cell(1, 0)
        cell_five = Cell(1, 1)

        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.game.add_cell(cell_three)
        self.game.add_cell(cell_four)
        self.game.add_cell(cell_five)

        self.game.get_next_iteration()
        self.assertFalse(cell_five.get_is_alive())

    def test_cell_with_three_neighbours_lives(self):
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 1)
        cell_three = Cell(0, 2)
        cell_four = Cell(1, 0)
        cell_five = Cell(1, 1)

        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.game.add_cell(cell_three)
        self.game.add_cell(cell_four)
        self.game.add_cell(cell_five)

        self.game.get_next_iteration()
        self.assertTrue(cell_four.get_is_alive())

    def test_dead_cell_with_exactly_three_neighbours_is_alive_again(self):
        cell_one = Cell(0, 0)
        cell_two = Cell(0, 1)
        cell_three = Cell(0, 2)
        cell_four = Cell(1, 0)
        cell_five = Cell(1, 1)
        cell_four.is_alive = False

        self.game.add_cell(cell_one)
        self.game.add_cell(cell_two)
        self.game.add_cell(cell_three)
        self.game.add_cell(cell_four)
        self.game.add_cell(cell_five)

        self.game.get_next_iteration()
        self.assertTrue(cell_four.get_is_alive())


if __name__ == '__main__':
    unittest.main()
