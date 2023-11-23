import random
from cards import *
import pygame


class Deck:
    def __init__(self, deck_ranks, deck_suits, deck_spritesheet):
        self.ranks = deck_ranks
        self.suits = deck_suits
        self.spritesheet = deck_spritesheet
        self.deck = self._create_deck()

    def _create_deck(self):
        deck = []
        for suit in self.suits:
            for rank in self.ranks:
                # Calculate the position of the card in the spritesheet
                x_pos = self.ranks.index(rank) * (CARD_WIDTH + 1)
                y_pos = self.suits.index(suit) * (CARD_HEIGHT + 1)

                # Create a Rect object for the card
                card_rect = pygame.Rect(x_pos, y_pos, CARD_WIDTH, CARD_HEIGHT)

                # Create a Card object and add it to the deck
                card = Card(rank, suit, self.spritesheet, card_rect)
                deck.append(card)
        return deck

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
