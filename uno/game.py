from uno.card import WildCard
from uno.card import SpecialCard
from uno.card import ColorCard
from uno.card import NumberCard
from uno.deck import Deck
from uno.player import ComputerPlayer
from uno.player import HumanPlayer
from random import randint
import logging

NUM_OF_INIT_CARDS = 7
NUM_OF_PLAYERS = 4


class Game:
    def __init__(self):
        logging.info('A game is created.')
        self.deck = Deck()
        self.players = []
        self.create_players()
        self.current_card = None

    def create_players(self):
        logging.info('Players are created.')
        # Creating Human player which waits for input every turn
        self.players.append(HumanPlayer())
        # Creating AI players which play available cards randomly
        for p in range(NUM_OF_PLAYERS-1):
            self.players.append(ComputerPlayer())

    def deal_cards(self):
        logging.info('Cards are dealt.')
        # Dealing cards for each player
        for p in self.players:
            for i in range(NUM_OF_INIT_CARDS):
                card = self.deck.draw_card()
                p.draw_card(card)
            # p.print_hand()

    def open_card(self):
        logging.info('First current card opened.')
        self.current_card = self.deck.draw_card()
        # Re-drawing a card in case it is a Wild Card
        while isinstance(self.current_card, WildCard):
            self.deck.insert_random(self.current_card)
            self.current_card = self.deck.draw_card()

    def start(self):
        logging.info('A game is started.')
        self.deal_cards()
        self.open_card()

