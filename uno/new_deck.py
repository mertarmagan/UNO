from enum import Enum, auto
from random import randint


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()


class Action(Enum):
    DRAW2 = auto()
    REVERSE = auto()
    SKIP = auto()


class WildAction(Enum):
    WILD = auto()
    WILD_DRAW4 = auto()


class Card:
    pass


class ColorCard(Card):
    def __init__(self, color: Color):
        self.color = color


class NumberCard(ColorCard):
    def __init__(self, color: Color, number: int):
        super().__init__(color)
        self.number = number

    def __repr__(self) -> str:
        return f"{self.color.name} - {self.number}"


class ActionCard(ColorCard):
    def __init__(self, color: Color, action: Action):
        super().__init__(color)
        self.action = action

    def __repr__(self) -> str:
        return f"{self.color.name} - {self.action.name}"


class WildCard(Card):
    def __init__(self, action: WildAction):
        self.action = action

    def __repr__(self) -> str:
        return f"{self.action.name}"


class Deck:
    _numbers = [n % 10 for n in range(1, 20)]
    _colors = [c for c in Color]
    _actions = [a for a in Action for _ in range(2)]
    _wild_actions = [a for a in WildAction for _ in range(4)]

    def __init__(self):
        number_cards = [
            NumberCard(color, number)
            for color in self._colors
            for number in self._numbers
        ]
        action_cards = [
            ActionCard(color, action)
            for color in self._colors
            for action in self._actions
        ]
        wild_cards = [WildCard(action) for action in self._wild_actions]
        self.cards = number_cards + action_cards + wild_cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, value):
        self.cards[position] = value

    def shuffle(self):
        n = len(self)
        for i in range(n - 1, 0, -1):
            j = randint(0, i)
            self[i], self[j] = self[j], self[i]
