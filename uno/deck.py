from uno.card import NumberCard
from uno.card import SpecialCard
from uno.card import WildCard
from uno.card_types.color import Color
from uno.card_types.special import Special
from uno.card_types.number import Number
from uno.card_types.wild import Wild
from random import randint


class Deck():
    def __init__(self):
        self.cards = []
        self.create_cards()

    def create_cards(self):
        self.init_color_card()
        self.init_wild_card()

        self.shuffle()
        # self.print()

    # TODO: DEBUG! There is a bug with shuffle, rarely its indices inside loop fall out of range.
    def shuffle(self):
        n = len(self.cards)
        for i in range(n - 1, 0, -1):
            j = randint(0, i + 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        return self.cards

    def draw_card(self, pile):
        rand_card = randint(0, len(self.cards) - 1)
        return pile.pop(rand_card)

    def print(self, pile):
        for c in pile:
            c.print()

    def init_color_card(self):
        for c in Color:
            for s in Special:
                self.cards.append(SpecialCard(Color(c), Special(s)))
                self.cards.append(SpecialCard(Color(c), Special(s)))
            for n in Number:
                self.cards.append(NumberCard(Color(c), Number(n)))
                if n != Number.ZERO:
                    self.cards.append(NumberCard(Color(c), Number(n)))

    def init_wild_card(self):
        for w in Wild:
            self.cards.append(WildCard(Wild(w)))
            self.cards.append(WildCard(Wild(w)))
            self.cards.append(WildCard(Wild(w)))
            self.cards.append(WildCard(Wild(w)))

    def insert_random(self, card, pile):
        index = randint(0, len(pile) - 1)
        pile.insert(index, card)
