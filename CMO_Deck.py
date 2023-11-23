import random
from cards import Card


class Deck:
    def __init__(self, ranks, suits, sprites):
        self.ranks = ranks
        self.suits = suits
        self.deck = [Card(rank, suit, sprites[suit][rank]) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_players):
        self.shuffle()
        hands = []
        for _ in range(num_players):
            hand = [self.deck.pop() for _ in range(10)]
            hands.append(hand)
        return hands

    def __repr__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n ' + card.__repr__()
        return 'The deck has ' + str(len(self.deck)) + ' cards:' + deck_comp
