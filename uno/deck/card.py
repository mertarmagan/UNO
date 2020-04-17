
class Card:
    def __init__(self):
        pass

class WildCard(Card):
    def __init__(self, typ):
        super().__init__()
        self.type = typ

class ColorCard(Card):
    def __init__(self, col):
        super().__init__()
        self.color = col

class NumberCard(ColorCard):
    def __init__(self, col, num):
        super().__init__(col)
        self.number = num

class SpecialCard(ColorCard):
    def __init__(self, col, typ):
        super().__init__(col)
        self.type = typ
