import sys
from random import randint

from uno.card import ColorCard, NumberCard, SpecialCard, WildCard
from uno.card_types.color import Color
from uno.card_types.wild import Wild
import logging

class Player:
    _id = 0

    def __init__(self):
        self.cards = []
        self.id = Player._id
        Player._id += 1

    def draw_card(self, card):
        self.cards.append(card)

    def print_hand(self):
        print('Player ' + str(self.id) + ' Hand:')
        for c in self.cards:
            c.print()
        print()

    def get_num_of_cards(self):
        return len(self.cards)

    def get_cards(self):
        return self.cards

    def get_id(self):
        return self.id

    def find_available_cards(self, cur_card, wild_color):
        avail_cards = []
        cards = self.cards
        wild_draw4_cards = []

        for c in cards:
            if isinstance(cur_card, ColorCard) and isinstance(c, ColorCard):
                if cur_card.color == c.color:
                    avail_cards.append(c)
                elif isinstance(cur_card, NumberCard) and isinstance(c, NumberCard):
                    if cur_card.number == c.number:
                        avail_cards.append(c)
                elif isinstance(cur_card, SpecialCard) and isinstance(c, SpecialCard):
                    if cur_card.type == c.type:
                        avail_cards.append(c)
            elif isinstance(cur_card, WildCard) and isinstance(c, ColorCard):
                if c.color == wild_color:
                    avail_cards.append(c)
            elif isinstance(c, WildCard) and c.type == Wild.WILD:
                avail_cards.append(c)
            elif isinstance(c, WildCard) and c.type == Wild.WILD_DRAW4:
                wild_draw4_cards.append(c)

        if not avail_cards:
            avail_cards = wild_draw4_cards

        return avail_cards

    def pick_color(self):
        color = None
        color_input = None
        index = 0
        for c in Color:
            print('   ' + str(index) + '-', end='')
            print(Color(c))
            index += 1

        if isinstance(self, HumanPlayer):
            # color_input = int(input("Please choose a color(0-R, 1-G, 2-B, 3-Y): "))
            color_input = int(sys.stdin.readline())
            while color_input not in range(0, 4):
                # color_input = int(input("Please choose a color(0-R, 1-G, 2-B, 3-Y): ")
                color_input = int(sys.stdin.readline())
        elif isinstance(self, ComputerPlayer):
            color_input = randint(0, 3)

        if color_input == 0:
            color = Color.RED
        elif color_input == 1:
            color = Color.GREEN
        elif color_input == 2:
            color = Color.BLUE
        elif color_input == 3:
            color = Color.YELLOW
        else:
            logging.warning('Invalid color input!')

        print('NEW COLOR PICKED:', color)
        return color

    def discard_card(self, card):
        self.cards.remove(card)

class HumanPlayer(Player):
    def __init__(self):
        super().__init__()


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

