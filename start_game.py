from games_versions.game_with_buffer import start_game as game1
from games_versions.game_without_buffer import start_game as game2


try:
    game1()
except ModuleNotFoundError:
    game2()