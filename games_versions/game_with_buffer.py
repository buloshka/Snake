from utils.connector import Game
from utils.constants import TICK
from time import sleep
from keyboard import wait
from curses import wrapper, curs_set


def main(stdscr):
    curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(int(TICK * 1000))

    game = Game()
    while True:
        stdscr.clear()
        game.game_processing()
        if game.is_over:
            print(game.over)
            return
        stdscr.addstr(game.cute_board)
        stdscr.refresh()
        sleep(TICK)


def start_game():
    wrapper(main)
    print('PRESS ENTER TO EXIT')
    wait(hotkey='enter')
