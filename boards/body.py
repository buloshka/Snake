from utils.constants import BodyPart, Move, Cells
from typing import Self


class SnakePart:
    def __init__(self, position: tuple[int, int], part_type: BodyPart = BodyPart.BODY) -> None:
        self.__current_x = position[0]
        self.__current_y = position[-1]
        self.__previous_x = None
        self.__previous_y = None
        self.__body_type = part_type

    @property
    def title(self) -> str:
        return self.__body_type.value

    @property
    def is_head(self) -> bool:
        return self.__body_type == BodyPart.HEAD

    @property
    def current_position(self) -> tuple[int, int]:
        return self.__current_x, self.__current_y

    @property
    def previous_position(self) -> tuple[int, int]:
        return self.__previous_x, self.__previous_y

    def do_step(self, position: tuple[int, int]) -> None:
        if not isinstance(position, tuple) and not len(position) != 2:
            return TypeError
        self.__previous_x = self.__current_x
        self.__previous_y = self.__current_y
        self.__current_x = position[0]
        self.__current_y = position[1]

    def is_touched_with(self, other: Self) -> bool:
        if not isinstance(other, SnakePart):
            return TypeError
        return self.current_position == other.current_position


class SnakeBody:
    def __init__(self, width: int, height: int, position: tuple[int, int]) -> None:
        self.__body = [SnakePart(position, BodyPart.HEAD)]
        self.__width = width
        self.__height = height
        self.__board = [[Cells.EMPTY for _ in range(width)] for _ in range(height)]

    @property
    def board(self) -> list[list[Cells]]:
        bodies = [part.current_position for i, part in self.bodies_positions]
        for i_row, row in enumerate(self.__board):
            for i_cell, cell in enumerate(row):
                if (i_cell, i_row) in bodies:
                    if self.head.current_position == (i_cell, i_row):
                        self.__board[i_row][i_cell] = Cells.HEAD
                    else:
                        self.__board[i_row][i_cell] = Cells.BODY
                else:
                    self.__board[i_row][i_cell] = Cells.EMPTY
        return self.__board

    @property
    def head(self) -> SnakePart:
        return self.__body[0]

    @property
    def body(self) -> list[SnakePart]:
        return self.__body

    @property
    def bodies_positions(self) -> list[tuple[int, SnakePart]]:
        return [(i, part) for i, part in enumerate(self.__body)]

    def add_part(self) -> None:
        self.__body.append(SnakePart(
            self.__body[-1].current_position,
        ))

    def head_is_touched(self) -> bool:
        head = self.__body[0]
        bodies = self.__body[1::]
        for body in bodies:
            if not body.is_touched_with(head):
                continue
            return True
        return False

    def check_x_y(self, x, y) -> tuple[int, int]:
        if x >= self.__width:
            x -= self.__width + 1
        elif x < 0:
            x += self.__width
        if y >= self.__height:
            y -= self.__height + 1
        elif y < 0:
            y += self.__height
        return x, y

    def do_step(self, step: Move) -> None:
        if not isinstance(step, Move):
            return TypeError
        for i, part in self.bodies_positions:
            if part.is_head:
                part_x, part_y = part.current_position
                to_position = self.check_x_y(part_x + step.value[0], part_y + step.value[-1])
                if to_position == part.previous_position:
                    return self.do_step(Move.opposite_direction(step))
                part.do_step(to_position)
                continue
            previous_part = self.__body[i - 1]
            part.do_step(previous_part.previous_position)
        return

    def __repr__(self) -> str:
        return f'SnakeBody([{", ".join(f"{body.title}{body.current_position}" for body in self.__body)}])'
