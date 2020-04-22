import threading

from uno.game import Game
from uno.ui import uno_frame
import logging
# Configuring the logging function to display proper messages in console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

def thread(game):
    game.start()

def run():
    game = Game()
    game_thread = threading.Thread(target=thread, args=[game])
    game_thread.start()
    # game.start()
    uno_frame.run(game)
    game_thread.join()
