import logging
import minesweeper as ms

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

print("This will play a single game and then quit.")
print("The minesweeper window needs focus to capture a key press.")
print()

num_games = 1
config = ms.GameConfig(16,16,32)
ai = ms.CSPAI()
viz = ms.PyGameVisualizer(pause=0.01, next_game_prompt=True)
result = ms.run_games(config, num_games, ai, viz).pop()
print('Game lasted {0} moves'.format(result.num_moves))
