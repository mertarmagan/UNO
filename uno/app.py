from uno.deck import deck
from uno.deck.card import NumberCard
from uno.deck.card import SpecialCard
from uno.deck.card import WildCard
from uno.deck.card import ColorCard

def run():
    d = deck.create()
    c = d.pop()
    print(c.getImageName())
    # c2 = d.pop()
    # print(c, type(c), c.id)
    # print(c2, type(c2), c2.id)
    #
    # if isinstance(c, NumberCard) and isinstance(c2, NumberCard):
    #     print(c.number, c2.number)
    #     print(c.number > c2.number)

