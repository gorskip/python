import random

class Player:
    def __init__(self):
        self.cards = []
        self.stack = []
        self.stack_usage = -1

    def pull_card(self) -> int:
        return self.cards.pop(0)

    def add_card(self, card):
        self.stack.append(card)
    
    def add_cards(self, card):
        self.stack.extend(card)

    def use_stack(self):
        self.stack_usage += 1
        random.shuffle(self.stack)
        self.cards.extend(self.stack)
        self.stack = []

    def can_play(self) -> bool:
        return self.has_cards_on_hand() or self.has_cards_on_stack()

    def has_cards_on_hand(self) -> bool:
        return len(self.cards) > 0
    
    def has_cards_on_stack(self) -> bool:
        return  len(self.stack) > 0

    def get_stack_usage(self):
        return self.stack_usage