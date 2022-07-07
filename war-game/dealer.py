import random
from player import Player

class Dealer:
    def __init__(self, cards):
        self.cards = cards
    
    def shufle(self, cards):
        random.shuffle(cards)

    def deal_cards(self, player_1: Player, player_2: Player):
        self.shufle(self.cards)
        for i in range(len(self.cards)):
            if (i % 2) == 0:
                player_1.add_card(self.cards[i])
            else:
                player_2.add_card(self.cards[i])
        player_1.use_stack()
        player_2.use_stack()
