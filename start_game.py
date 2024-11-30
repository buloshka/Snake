try:
    from games_versions.game_with_buffer import start_game as game1
    game1()
except ModuleNotFoundError:
    from games_versions.game_without_buffer import start_game as game2
    game2()