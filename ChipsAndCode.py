import pygame 
import random

##constant lists for the card suit and rank
SUIT = ["hearts", "diamonds", "spades", "clubs"]

RANK = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

GamePhase = ["blinds", "preFlop", "flop", "turn", "river"]

class Player:

    def __init__(self, name):

        self.chips = 1000

        self.name = name

        self.hand = []

        self.folded = False

    def recieveCard(self, card: Card):

        self.hand.append(card)


class Card:
    

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.image = pygame.image.load(f"assets/cards/{rank}_of_{suit}.png")

class Deck:

    #constructor
    def __init__(self):

        self.cards = [Card(r,s) for r in RANK for s in SUIT]
        self.shuffle

    #method for shuffling the deck after it is created
    def shuffle(self):

        random.shuffle(self.cards)

    #method for drawing a card from the deck
    def drawCard(self) -> Card:

        return self.cards.pop()
    
    #method for dealing cards to players
    def deal(self, player, numCards):

        for c in range(numCards):

            Player.recieveCard(self.drawCard())

#class for an active game, includes info for the game such as the current phase, current pot, etc..
class ActiveGame:

    def __init__(self, player):
        
        self.currentPlayer = player
        self.phase = GamePhase[0]
        self.pot = 0
        self.deck = []
      

