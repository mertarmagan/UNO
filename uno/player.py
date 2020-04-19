class Player():
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


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()


class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

