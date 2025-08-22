import sys
from enum import Enum, auto
from typing import List

from loguru import logger

from uno.new_deck import Card, Deck

# Log configurations
LOG_LEVEL = "DEBUG"
LOG_FORMAT = "{time:YYYY-MM-DD HH:mm:ss.SSS!UTC} | {level} | {message}"

# Remove default logger
logger.remove()
# Add stderr logger
logger.add(
    sys.stderr,
    level=LOG_LEVEL,
    format=LOG_FORMAT,
)


class Direction(Enum):
    CLOCKWISE = auto()
    COUNTER_CLOCKWISE = auto()


class Player:
    __id = 0

    def __init__(self):
        self.cards = []
        self.id = Player.__id
        Player.__id += 1
        logger.debug(f"{self} created.")

    def __len__(self):
        return len(self.cards)

    def draw_card(self, card: Card):
        self.cards.append(card)

    def print_hand(self):
        logger.debug(f"{self} cards: {self.cards}")


class HumanPlayer(Player):
    def __repr__(self) -> str:
        return f"Player {self.id} (Human)"


class ComputerPlayer(Player):
    def __repr__(self) -> str:
        return f"Player {self.id} (Computer)"


class Pile:
    def __init__(self):
        logger.debug(f"{self} created.")

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position: int):
        return self.cards[position]

    def draw(self):
        top_card = None
        if len(self.cards) > 0:
            top_card = self.cards.pop()

        return top_card


class DrawPile(Pile):
    def __init__(self, cards: List[Card]):
        self.cards = cards
        super().__init__()

    def __repr__(self) -> str:
        return f"Draw pile ({len(self.cards)} cards)"


class DiscardPile(Pile):
    def __init__(self):
        self.cards = []
        super().__init__()

    def __repr__(self) -> str:
        return f"Discard pile ({len(self.cards)} cards)"


class GameController:
    NUM_OF_INITIAL_CARDS = 7

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.players = [HumanPlayer()] + [ComputerPlayer() for _ in range(3)]
        self.draw_pile = DrawPile(self.deck.cards)
        self.discard_pile = DiscardPile()

        # TODO: keep player instance or index?
        self.dealer_index = 0
        self.player_index = 1
        self.direction = True

    def deal_cards(self, players: List[Player] = None, pile: DrawPile = None):
        logger.info("Dealing cards..")
        for _ in range(self.NUM_OF_INITIAL_CARDS):
            for player in self.players:
                player.draw_card(self.draw_pile.draw())

    def start(self):
        logger.info("Game started!")
        self.deal_cards()
        self.print_hands()
        pass

    def print_hands(self):
        for player in self.players:
            player.print_hand()
