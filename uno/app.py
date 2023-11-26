# -*- coding: utf-8 -*-
import logging

from uno.game import Game
from uno.ui.uno_frame import UI

# Configuring the logging function to display proper messages in console
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


def game_thread(frame, root):
    game = Game(frame, root)
    game.start()


def ui_thread(ui):
    ui.run()


def run():
    UI(game_thread)
