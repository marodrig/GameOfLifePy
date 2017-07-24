class Cell:
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __hash__(self) -> int:
        return 31 * hash((self.x, self.y))

    def __eq__(self, other: object) -> bool:
        return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        return "X cord: %d Y cord: %d" % (self.x, self.y)

    def __init__(self, x: int, y: int):
        self.x = int(x)
        self.y = int(y)
        self.is_alive = True

    def get_cord_y(self) -> int:
        return self.y

    def get_cord_x(self) -> int:
        return self.x

    def get_is_alive(self) -> bool:
        return self.is_alive
