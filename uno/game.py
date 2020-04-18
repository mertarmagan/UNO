from uno.deck import Deck
from uno.player import ComputerPlayer
from uno.player import HumanPlayer

NUM_OF_INIT_CARDS = 7
NUM_OF_PLAYERS = 4

class Game():
    players = []
    deck = []

    def __init__(self):
        self.deck = Deck()
        self.create_players()
        self.deal_cards()

    def create_players(self):
        # Creating Human player which waits for input every turn
        self.players.append(HumanPlayer())
        # Creating AI players except one Human Player
        for p in range(NUM_OF_PLAYERS-1):
            self.players.append(ComputerPlayer())

    def deal_cards(self):
        for p in self.players:
            for i in range(NUM_OF_INIT_CARDS):
                card = self.deck.draw_card()
                p.draw_card(card)
            # p.print_hand()

    def start(self):
        pass


