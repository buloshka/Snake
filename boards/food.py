from utils.constants import Cells
from random import randint


class Berry:
    def __init__(self, width: int, height: int) -> None:
        self.__width = width
        self.__height = height
        self.__x, self.__y = 0, 0
        self.__board = [[Cells.EMPTY for _ in range(width)] for _ in range(height)]
        self.put_berry_on_board()

    @property
    def board(self) -> list[list[Cells]]:
        return self.__board

    @property
    def position(self) -> tuple[int, int]:
        return self.__x, self.__y

    def put_berry_on_board(self) -> None:
        self.__board = [[Cells.EMPTY for _ in range(self.__width)] for _ in range(self.__height)]
        self.__x, self.__y = randint(0, 29), randint(0, 29)
        self.__board[self.__y][self.__x] = Cells.FOOD
