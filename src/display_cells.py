from src.game_of_life import GameOfLife


class DisplayCells:
    def __init__(self):
        self.game = GameOfLife()
        self.game_board = [[]]

    def init_board(self, rows: int, cols: int) -> None:
        self.game_board = [['.' for _ in range(cols)] for _ in range(rows)]

    def display_board(self) -> list:
        for each in self.game.set_cells:
            if each.is_alive:
                self.game_board[each.get_cord_x()][each.get_cord_y()] = '*'
        return self.game_board
