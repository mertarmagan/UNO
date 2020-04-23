from uno.ui.uno_frame import UI
from uno.game import Game
import threading
import logging
# Configuring the logging function to display proper messages in console
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

def game_thread(frame):
    game = Game(frame)
    game.start()

def ui_thread(ui):
    ui.run()

def run():
    # g = threading.Thread(target=game_thread, args=[])
    ui = UI(game_thread)
    # u = threading.Thread(target=ui_thread, args=[ui])
    # u.start()
    # game = Game(ui.frame)
    # g.start()
    # g.join()
