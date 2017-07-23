from src.cell import Cell


class GameOfLife:
    def __init__(self):
        self.set_cells = set()
        pass

    def add_cell(self, cell: Cell):
        self.set_cells.add(cell)

    def get_near_neighbours(self, cell: Cell) -> list:
        valid_near_neighbours_list = list()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                c = Cell(cell.get_cord_x() + dx, int(cell.get_cord_y() + dy))
                if c != cell:
                    valid_near_neighbours_list.append(c)
        return valid_near_neighbours_list

    def get_neighbours(self, cell: Cell) -> list:
        list_of_neighbours = list()
        for c in self.set_cells:
            if c in self.get_near_neighbours(cell):
                list_of_neighbours.append(c)
        return list_of_neighbours

    def get_next_iteration(self):
        for c in self.set_cells:
            c.is_alive = False
