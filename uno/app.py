from uno.game import Game
import logging
# Configuring the logging function to display proper messages in console
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def run():
    g = Game()
    g.start()
    g.current_card.print()
    # g.deck.print()
