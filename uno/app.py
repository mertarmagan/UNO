from uno.game import Game
from uno.ui import uno_frame
import logging
# Configuring the logging function to display proper messages in console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def run():
    g = Game()
    g.start()
    uno_frame.run(g)
    print(g.get_current_card())
    print(g.get_current_player())
