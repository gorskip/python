from dealer import Dealer
from player import Player
import statistics
import time

class WarGame(object):

    number_of_decks = 1
    number_of_games = 10000

    def buildDeck(self):
        deck = []
        for n in range(0, self.number_of_decks):
            for cardValue in range(2,15):   
                deck.extend([cardValue, cardValue, cardValue, cardValue])
        return deck

    def run(self):
        start_time = time.time()
        cards = self.buildDeck()
        dealer = Dealer(cards)

        winner_stack_usage = []
        looser_stack_usage = []
        
        for n in range(0, self.number_of_games):
            
            player_1 = Player()
            player_2 = Player()

            dealer.deal_cards(player_1, player_2)
            self.play(player_1, player_2)

            if(player_1.can_play()):
                winner_stack_usage.append(player_1.get_stack_usage())
                looser_stack_usage.append(player_2.get_stack_usage())
            else:
                winner_stack_usage.append(player_2.get_stack_usage())
                looser_stack_usage.append(player_1.get_stack_usage())

            winner_stack_usage.append(player_1.get_stack_usage())
            looser_stack_usage.append(player_2.get_stack_usage())

        print("Median value of stack usage of the winner", statistics.median(winner_stack_usage))
        print("Mean value of stack usage of the winner", statistics.mean(winner_stack_usage))
        print("Max times a winner used his stack", max(winner_stack_usage))
        print("Min times a winner used his stack", min(winner_stack_usage))
        print()
        print("Median of stack usage of the looser", statistics.median(looser_stack_usage))
        print("Mean value of stack usage of the looser", statistics.mean(looser_stack_usage))
        print("Max times a looser used his stack", max(looser_stack_usage))
        print("Min times alooser used his stack", min(looser_stack_usage))
        print("--- %s seconds ---" % (time.time() - start_time))

        
    def play(self, player_1: Player, player_2: Player, blind_cards = []):
        while(player_1.can_play() and player_2.can_play()):
            
            if not player_1.has_cards_on_hand():
                player_1.use_stack()

            if not player_2.has_cards_on_hand():
                player_2.use_stack()
            
            p1_card = player_1.pull_card()
            p2_card = player_2.pull_card()

            if p1_card > p2_card:
                player_1.add_cards(blind_cards)
                blind_cards = []
                player_1.add_card(p2_card)
                player_1.add_card(p1_card)
                continue
            if p2_card > p1_card:
                player_2.add_cards(blind_cards)
                blind_cards = []
                player_2.add_card(p1_card)
                player_2.add_card(p2_card)
                continue
            else:
                if player_1.can_play() and player_2.can_play():
                    if not player_1.has_cards_on_hand():
                        player_1.use_stack()
                    blind_cards.append(player_1.pull_card())
                    if not player_2.has_cards_on_hand():
                        player_2.use_stack()
                    blind_cards.append(player_2.pull_card())
                    self.play(player_1, player_2, blind_cards)
                else:
                    continue
        

if __name__ == '__main__':
    WarGame().run()