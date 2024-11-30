from utils.game_statistics import Item
from enum import StrEnum, Enum


class Cells(StrEnum):
    EMPTY = "🟫"
    HEAD = "🟧"
    BODY = "🟪"
    FOOD = "🟥"


class BodyPart(StrEnum):
    HEAD = 'Head'
    BODY = 'Body'


class Move(Enum):
    WAIT = (0, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    @staticmethod
    def opposite_direction(other: 'Move') -> 'Move':
        if not isinstance(other, Move):
            return TypeError
        return {
            Move.UP: Move.DOWN,
            Move.DOWN: Move.UP,
            Move.LEFT: Move.RIGHT,
            Move.RIGHT: Move.LEFT,
        }.get(other)


FRAMES = 2
TICK = 1 / FRAMES

FOOD_COUNT = 3
FOOD_BONUS = 1

WIDTH = 10
HEIGHT = 10

START_X = 0
START_Y = 0

REWARDS = Item(Cells.FOOD, 30)

LOOSE_TEXT = [
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥',
    '🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥',
    '🟥⬜🟥⬜🟥⬜🟥🟥🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥',
    '🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜⬜⬜🟥⬜⬜⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜⬜🟥⬜🟥⬜🟥⬜🟥⬜⬜⬜🟥⬜🟥⬜⬜⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥🟥🟥⬜⬜🟥🟥⬜⬜⬜⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥🟥🟥⬜🟥',
    '🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥',
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥',
]

WIN_TEXT = [
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥',
    '🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥',
    '🟥⬜🟥⬜🟥⬜🟥🟥🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜⬜⬜⬜🟥⬜🟥🟥🟥⬜🟥⬜⬜🟥⬜🟥',
    '🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜🟥⬜⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜🟥🟥⬜🟥⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜🟥🟥⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜⬜⬜⬜🟥⬜🟥⬜🟥⬜⬜🟥⬜🟥⬜🟥⬜🟥🟥⬜🟥',
    '🟥⬜⬜🟥⬜⬜🟥🟥🟥⬜⬜🟥🟥⬜⬜⬜⬜⬜⬜🟥⬜🟥⬜⬜⬜🟥🟥🟥⬜🟥⬜⬜🟥⬜🟥',
    '🟥⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟥',
    '🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥',
]

CLEAR = 'cls'
