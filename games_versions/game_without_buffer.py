from utils.connector import Game
from utils.constants import TICK, CLEAR
from os import system
from time import sleep
from keyboard import wait


def main():
    game = Game()
    while True:
        system(CLEAR)
        game.game_processing()
        if game.is_over:
            print(game.over)
            return
        print(game.cute_board)
        sleep(TICK)


def start_game():
    main()
    print('PRESS ENTER TO EXIT')
    wait(hotkey='enter')
