from uno.deck.card import NumberCard
from uno.deck.card import SpecialCard
from uno.deck.card import WildCard
from uno.deck.card_types.color import Color
from uno.deck.card_types.special import Special
from uno.deck.card_types.number import Number
from uno.deck.card_types.wild import Wild
from random import randint


def init():
    card_deck = []

    init_color_card(card_deck)
    init_wild_card(card_deck)

    print_deck(card_deck)

    return card_deck


def draw_card(deck):
    rand_card = randint(0, len(deck)-1)
    return deck.pop(rand_card)


def print_deck(card_deck):
    for c in card_deck:
        if isinstance(c, SpecialCard):
            print('Special Card - typ:', c.type, 'col:', c.color, 'id:', c.id)
        elif isinstance(c, NumberCard):
            print('Number Card - num:', c.number, ' col:', c.color, 'id:',c.id)
        elif isinstance(c, WildCard):
            print('Wild Card - typ:', c.type, 'id:', c.id)


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
