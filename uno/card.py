class Card:
    _id = 0

    def __init__(self):
        self.id = Card._id
        Card._id += 1

    def getImageName(self):
        path = ''
        if isinstance(self, NumberCard):
            path = self.color.value + '_' + str(self.number.value)
        elif isinstance(self, SpecialCard):
            path = self.color.value + '_' + self.type.value
        elif isinstance(self, WildCard):
            path = self.type.value
        return path

    def print(self):
        if isinstance(self, SpecialCard):
            print('Special Card - typ:', self.type, 'col:', self.color, 'id:', self.id)
        elif isinstance(self, NumberCard):
            print('Number Card - num:', self.number, ' col:', self.color, 'id:', self.id)
        elif isinstance(self, WildCard):
            print('Wild Card - typ:', self.type, 'id:', self.id)

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
