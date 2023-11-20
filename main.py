class CMODeck:
    def __init__(self):
        # Define the ranks and suits
        self.ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.french_suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds']
        self.italian_suits = ['Cups', 'Staves', 'Swords', 'Coins']

        # Create the deck
        self.deck = [{'rank': rank, 'suit': suit} for suit in self.french_suits + self.italian_suits for rank in self.ranks]

        # Verify the deck
        print(f'The deck has {len(self.deck)} cards.')
        for card in self.deck:
            print(f"{card['rank']} of {card['suit']}")

my_deck = CMODeck()
