import pygame
import random
import CMO_Deck
import game_loop



# def load_sprites(deck):
#     # This function should load your card images (sprites) and assign them to the cards in the deck
#     pass

def shuffle_and_deal(deck, num_players):
    # This function should shuffle the deck and deal the cards to the players
    pass

def main():
    pygame.init()

    # Set up some constants
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    CARD_WIDTH = 50
    CARD_HEIGHT = 100

    # Create the window
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Create the deck
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Clubs', 'Spades', 'Diamonds', 'Cups', 'Staves', 'Swords', 'Coins']
    sprites = {...}  # Fill in with your sprites
    deck = CMO_Deck.Deck(ranks, suits, sprites)

    # Load the sprites
    # load_sprites(deck)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here

        # Draw the window
        window.fill((255, 255, 255))  # Fill the window with white

        # Draw the cards
        for card in deck.deck:
            window.blit(card.sprite, (0, 0))  # This should actually position the cards correctly

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
