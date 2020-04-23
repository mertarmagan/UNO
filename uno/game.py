import sys
import time

from uno.card import WildCard, SpecialCard
from uno.card_types.special import Special
from uno.card_types.wild import Wild
from uno.deck import Deck
from uno.player import ComputerPlayer
from uno.player import HumanPlayer
from random import randint

import logging

NUM_OF_INIT_CARDS = 7
NUM_OF_PLAYERS = 4


class Game:
    def __init__(self, frame):
        logging.info('A game is created.')
        self.frame = frame  # UI thread's Frame
        self.deck = Deck()  # deck of default cards
        self.players = []  # list of players including Computer and Human
        self.human_player = None

        self.create_players()

        self.draw_pile = self.deck.cards  # pile of cards have never played (list of cards)
        self.discard_pile = []  # pile of tossed cards in the middle (list of cards)

        self.current_player_ind = -1

        self.direction = True
        self.wild_color = None

        self.skipped = False
        self.finished = False

    def create_players(self):
        logging.info('Players are created.')
        # Creating Human player which waits for input every turn
        self.human_player = HumanPlayer()
        self.players.append(self.human_player)
        # Creating AI players which play available cards randomly
        for p in range(NUM_OF_PLAYERS - 1):
            self.players.append(ComputerPlayer())

    def deal_cards(self):
        logging.info('Cards are dealt.')
        # Dealing cards for each player
        for index, p in enumerate(self.players):
            for i in range(NUM_OF_INIT_CARDS):
                card = self.deck.draw_card(self.draw_pile)
                p.draw_card(card)
            self.frame.update_num_of_cards(index, NUM_OF_INIT_CARDS)

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
        return randint(0, len(self.players) - 1)

    def start(self):
        logging.info('A game is started.')
        self.deal_cards()

        self.frame.show_hand(self.human_player.get_cards())

        self.print_hands()
        self.open_card()
        self.current_player_ind = self.pick_starter()

        print('\n**************************** GAME STARTED ***************************')
        print('Player:', type(self.get_current_player()).__name__, '(' + str(self.get_current_player_index()) + ')')
        self.frame.highlight_player(self.get_current_player_index())

        current_card = self.get_current_card()
        self.frame.update_cur_card(current_card)

        print('Top Card:', end=' ')
        current_card.print()
        if isinstance(current_card, SpecialCard):
            self.current_player_ind = (self.current_player_ind - 1) % NUM_OF_PLAYERS
            if current_card.type == Special.DRAW2:
                self.special_draw2()
            elif current_card.type == Special.REVERSE:
                self.special_reverse()
            elif current_card.type == Special.SKIP:
                self.special_skip()
            self.change_turn()
        else:
            print('\n**************************** PLAYER CONT. ***************************')

        while not self.finished:
            print('Player:', type(self.get_current_player()).__name__, '(' + str(self.get_current_player_index()) + ')')
            self.frame.highlight_player(self.get_current_player_index())
            print("Num. of cards:", len(self.get_current_player().cards))
            current_card = self.discard_card()

            self.frame.update_num_of_cards(self.get_current_player_index(), len(self.get_current_player().cards))

            self.frame.update_cur_card(current_card)
            print('Top Card:', end=' ')
            current_card.print()
            if not self.skipped:
                if isinstance(current_card, SpecialCard):
                    if current_card.type == Special.DRAW2:
                        self.special_draw2()
                    elif current_card.type == Special.REVERSE:
                        self.special_reverse()
                    elif current_card.type == Special.SKIP:
                        self.special_skip()
                elif isinstance(current_card, WildCard):
                    if current_card.type == Wild.WILD:
                        self.wild()
                    elif current_card.type == Wild.WILD_DRAW4:
                        self.wild_draw4()

            self.change_turn()

    def get_current_card(self):
        # Returning the last element on discard pile or None in case it is empty
        return self.discard_pile[-1] if self.discard_pile else None

    def get_current_player(self):
        return self.players[self.current_player_ind]

    def get_next_player(self):
        return self.players[self.get_next_player_index()]

    def get_current_player_index(self):
        return self.current_player_ind

    def get_next_player_index(self):
        if self.direction:
            return (self.get_current_player_index() + 1) % NUM_OF_PLAYERS
        else:
            return (self.get_current_player_index() - 1) % NUM_OF_PLAYERS

    def change_turn(self):
        if self.direction:
            self.current_player_ind = (self.current_player_ind + 1) % NUM_OF_PLAYERS
        else:
            self.current_player_ind = (self.current_player_ind - 1) % NUM_OF_PLAYERS
        self.frame.update_num_of_cards(self.get_current_player_index(), len(self.get_current_player().cards))
        self.frame.show_hand(self.human_player.get_cards())
        print('\n**************************** NEXT PLAYER ***************************')

    def special_skip(self):
        self.change_turn()

    def special_draw2(self):
        next_player = self.get_next_player()
        for i in range(2):
            card = self.deck.draw_card(self.draw_pile)
            next_player.draw_card(card)
        self.change_turn()

    def special_reverse(self):
        self.direction = not self.direction

    def wild(self):
        cur_player = self.get_current_player()
        self.wild_color = cur_player.pick_color()

    def wild_draw4(self):
        cur_player = self.get_current_player()
        self.wild_color = cur_player.pick_color()

        next_player = self.get_next_player()
        for i in range(4):
            card = self.deck.draw_card(self.draw_pile)
            next_player.draw_card(card)
        self.change_turn()

    def discard_card(self):
        current_player = self.get_current_player()
        available = current_player.find_available_cards(self.get_current_card(), self.wild_color)

        if not available:
            card = self.deck.draw_card(self.draw_pile)
            current_player.draw_card(card)
            self.frame.show_hand(self.human_player.get_cards())
            print('No available, drawing a card: ', end='')
            card.print()

        available = current_player.find_available_cards(self.get_current_card(), self.wild_color)

        if available:
            print('Available Cards:')
            for index in range(len(available)):
                print('   ' + str(index) + '-', end='')
                available[index].print()

            if isinstance(current_player, HumanPlayer):
                # card_input = int(input('Select a card:'))
                card_input = int(sys.stdin.readline())
            elif isinstance(current_player, ComputerPlayer):
                time.sleep(3)
                card_input = randint(0, len(available) - 1)

            disc_card = available[card_input]
            current_player.discard_card(disc_card)
        else:
            time.sleep(1)
            print('No available again, skipping player!')
            self.skipped = True
            return self.get_current_card()

        if len(current_player.cards) == 0:
            self.finished = True

        self.discard_pile.append(disc_card)
        self.skipped = False
        return disc_card

    def print_hands(self):
        for p in self.players:
            p.print_hand()
