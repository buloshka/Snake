from boards.board import Board
from utils.game_statistics import Statistic, Item
from boards.body import SnakeBody
from utils.move_controller import MoveController
from boards.food import Berry
from time import perf_counter
from utils.constants import Cells
from utils.constants import (FOOD_COUNT, REWARDS, FOOD_BONUS,
                       WIDTH, HEIGHT,
                       START_Y, START_X,
                       LOOSE_TEXT, WIN_TEXT)



class Game:
    def __init__(self) -> None:
        self.__start: float = perf_counter()
        self.__stats = Statistic(REWARDS)
        self.__board = Board(WIDTH, HEIGHT)
        self.__snake = SnakeBody(WIDTH, HEIGHT, (START_X, START_Y))
        self.__move = MoveController()
        self.__food = [Berry(self.__board.width, self.__board.height) for _ in range(FOOD_COUNT)]

    @property
    def is_over(self) -> bool:
        return self.is_win or self.is_loose

    @property
    def is_loose(self) -> bool:
        return self.__snake_touch_snake() and len(self.__snake.body) > 4

    @property
    def is_win(self) -> bool:
        rewards: Item = self.__stats.items[0]
        return rewards.is_higher_or_equal_than_max

    @property
    def over(self) -> str:
        minutes: int = int((perf_counter() - self.__start) // 60)
        seconds: int = int((perf_counter() - self.__start) - minutes * 60)
        message = {
            'Время прохождения': f'  минуты - {minutes}\n{" " * 21}секунды - {seconds}',
            'Кол-во ягод на доске': f'{FOOD_COUNT}',
            'Съедено ягод': f'{self.__stats.items[0].current_value}',
        }
        message = '\n'.join(f'{key}: {value}' for key, value in message.items())
        func_over = self.win if self.is_win else self.loose
        return func_over(message)

    @property
    def cute_board(self) -> str:
        food = None
        for berry in self.__food:
            if not food:
                food = berry.board
                continue
            food = self.merge_boards(food, berry.board)

        board = self.merge_boards(self.__snake.board, self.merge_boards(self.__board.board, food))
        cute_board = '\n'.join(f'{"".join(cell.value for cell in row)}' for row in board)
        stats = self.__stats.info_stats
        head_position = f'user: {self.__snake.head.current_position}'
        move_direction = f'move direction: {self.__move.last_pressed}'
        return '\n'.join([move_direction, head_position, stats, cute_board])

    @staticmethod
    def loose(message=''):
        new_line = '\n'
        add = 'Ты столкнулся сам с собой!'
        return f"{new_line.join(LOOSE_TEXT)}\n({add})\n{message}"

    @staticmethod
    def win(message=''):
        new_line = '\n'
        add = f'Ты скушал достаточно ягод и победил!'
        return f"{new_line.join(WIN_TEXT)}\n({add})\n{message}"

    @staticmethod
    def merge_boards(board1: list[list[Cells]], board2: list[list[Cells]]) -> list[list[Cells]]:
        if len(board1) != len(board2) or any(len(row1) != len(row2) for row1, row2 in zip(board1, board2)):
            raise ValueError("Доски должны быть одинакового размера")
        result_board = [
            [
                cell1 if cell1 != Cells.EMPTY else cell2
                for cell1, cell2 in zip(row1, row2)
            ]
            for row1, row2 in zip(board1, board2)
        ]
        return result_board

    def game_processing(self) -> None:
        self.__snake.do_step(self.__move.last_pressed)
        self.__snake_on_food()

    def __snake_on_food(self) -> None:
        head = self.__snake.head.current_position
        for berry in self.__food:
            if berry.position != head:
                continue
            rewards = self.__stats.items[0]
            if rewards.in_min_max and not rewards.is_higher_or_equal_than_max or rewards.current_value == rewards.min_value:
                rewards.current_value += FOOD_BONUS
            bodies = [body.previous_position for body in self.__snake.body]
            berry.put_berry_on_board(bodies)
            self.__snake.add_part()
            return True
        return False

    def __snake_touch_snake(self) -> bool:
        return self.__snake.head_is_touched()
