class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.french_suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        self.italian_suits = ['Cups', 'Staves', 'Swords', 'Coins']
        self.deck = [Card(rank, suit) for suit in self.french_suits + self.italian_suits for rank in self.ranks]

    def __repr__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__repr__()
        return 'The deck has ' + str(len(self.deck)) + ' cards:' + deck_comp
