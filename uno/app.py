import threading
from uno.ui.uno_frame import UI
from uno.game import Game
from uno.ui import uno_frame
import logging
# Configuring the logging function to display proper messages in console


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def thread(game):
    game.start()


def run():
    ui_thread = UI()
    game = Game()
    game_thread = threading.Thread(target=thread, args=[game])
    game_thread.start()
    game_thread.join()
