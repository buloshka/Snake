import keyboard
from utils.constants import Move, TICK
from time import sleep


class MoveController:
    def __init__(self) -> None:
        self.__last_pressed = Move.WAIT
        self.__setup_key_listeners()

    def __setup_key_listeners(self) -> None:
        keyboard.on_press_key("w", lambda _: self.__update_last_pressed(Move.UP))
        keyboard.on_press_key("s", lambda _: self.__update_last_pressed(Move.DOWN))
        keyboard.on_press_key("a", lambda _: self.__update_last_pressed(Move.LEFT))
        keyboard.on_press_key("d", lambda _: self.__update_last_pressed(Move.RIGHT))

    def __update_last_pressed(self, move: Move) -> None:
        if move == Move.opposite_direction(self.last_pressed):
            return 
        self.__last_pressed = move

    @property
    def last_pressed(self) -> Move:
        return self.__last_pressed

    @staticmethod
    def wait_for_tick() -> None:
        sleep(TICK)
