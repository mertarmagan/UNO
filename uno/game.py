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
        self.deck = Deck()  # deck of default cards
        self.players = []  # list of players including Computer and Human
        self.create_players()

        self.draw_pile = self.deck.cards  # pile of cards have never played (list of cards)
        self.discard_pile = []  # pile of tossed cards in the middle (list of cards)

        self.current_player = None
        self.current_turn = -1

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
                card = self.deck.draw_card(self.draw_pile)
                p.draw_card(card)
            # p.print_hand()

    def open_card(self):
        logging.info('First card drawn for the startup.')
        current_card = self.deck.draw_card(self.draw_pile)
        # Re-drawing a card in case it is a Wild Card
        while isinstance(current_card, WildCard):
            logging.warning('A WILD CARD drawn and re-drawing a card for the startup!')
            self.deck.insert_random(current_card, self.draw_pile)
            current_card = self.deck.draw_card(self.draw_pile)
        self.discard_pile.append(current_card)

    def pick_starter(self):
        # Be careful with randint function, start <= N <= end (all inclusive range)
        return randint(0, len(self.players)-1)

    def start(self):
        logging.info('A game is started.')
        self.deal_cards()
        self.open_card()
        self.current_turn = 0
        self.current_player = self.pick_starter()

    def get_current_card(self):
        # Returning the last element on discard pile or None in case it is empty
        return self.discard_pile[-1] if self.discard_pile else None

    def get_current_player(self):
        return self.players[self.current_player]

    def get_current_turn(self):
        return self.current_turn

    def change_turn(self):
        self.current_player = (self.current_player + 1) % NUM_OF_PLAYERS
