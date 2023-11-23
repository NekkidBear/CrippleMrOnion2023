import pygame

# Initialize Pygame
pygame.init()

# Load the spritesheet
spritesheet = pygame.image.load('Sprites/cripple_mr__onion_deck_by_greysonx_dd3pxu0.png')

# Define the size of each card sprite
CARD_WIDTH = 72
CARD_HEIGHT = 96

# Define the suits and ranks
suits = ['hearts', 'diamonds', 'clubs', 'spades', 'cups', 'swords', 'staves', 'coins']
ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']

# Create a dictionary to map card names to their images
cards = {}

for i, suit in enumerate(suits):
    for j, rank in enumerate(ranks):
        # Calculate the position of the card in the spritesheet
        x = j * (CARD_WIDTH + 1)
        y = i * (CARD_HEIGHT + 1)

        # Create a Rect object for the card
        card_rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

        # Extract the card image from the spritesheet
        card_image = spritesheet.subsurface(card_rect)

        # Add the card to the dictionary
        card_name = f"{rank} of {suit}"
        cards[card_name] = card_image
