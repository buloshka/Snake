from utils.constants import Cells


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__cells = [[Cells.EMPTY for _ in range(width)] for _ in range(height)]

    @property
    def width(self) -> int:
        return self.__width

    @property
    def height(self) -> int:
        return self.__height

    @property
    def board(self) -> list[list[Cells]]:
        return self.__cells
