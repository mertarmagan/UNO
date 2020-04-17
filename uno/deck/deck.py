from uno.deck.card import NumberCard
from uno.deck.card import SpecialCard
from uno.deck.card import WildCard
from uno.deck.card_types.color import Color
from uno.deck.card_types.special import Special
from uno.deck.card_types.number import Number
from uno.deck.card_types.wild import Wild


def init():
    card_deck = []

    init_color_card(card_deck)
    init_wild_card(card_deck)

    return card_deck


def print_deck(card_deck):
    for c in card_deck:
        if isinstance(c, SpecialCard):
            print('Special Card - typ:', c.type, ' col:', c.color)
        elif isinstance(c, NumberCard):
            print('Number Card - num:', c.number, ' col:', c.color)
        elif isinstance(c, WildCard):
            print('Wild Card - typ:', c.type)


def init_color_card(card_deck):
    for c in Color:
        for s in Special:
            card_deck.append(SpecialCard(Color(c), Special(s)))
            card_deck.append(SpecialCard(Color(c), Special(s)))
        for n in Number:
            card_deck.append(NumberCard(Color(c), Number(n)))
            if n != Number.ZERO:
                card_deck.append(NumberCard(Color(c), Number(n)))


def init_wild_card(card_deck):
    for w in Wild:
        card_deck.append(WildCard(Wild(w)))
        card_deck.append(WildCard(Wild(w)))
        card_deck.append(WildCard(Wild(w)))
        card_deck.append(WildCard(Wild(w)))