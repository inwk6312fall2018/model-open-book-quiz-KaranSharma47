import sys
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Game:

    def __init__(self, name: str):
        self.hand = []
        self.name = name

    def __str__(self):
        return self.name

class BlackjackGame:

    def __init__(self, players: List[Player]):
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        for i in range(52)
            burned = self.deck.draw()
            if burn == 10:
                self.deck.discard(burn)
        self.players = players
        self.points = {}
        print("formed a game with {} players.".format(len(self.players)))

    def blackjack(self):
        """
        This block contains main blackjack game play.

        """
        print("start")
        print("Shuffling...")
        self.deck.discard('10')
        self.deck.shuffle()
        print("shuffled!")
        print("Deal")
        self.deal()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print(" finalizing winner")
            self.find_winner()

    def deal(self):
        """
        Deals five cards to each player.
        """
        for _ in range(5):
            for p in self.players:
                newcard = self.deck.draw()
                p.hand.append(newcard)
                print("Dealt {} the {}.".format(p.name, str(newcard)))

    def winner(self):
        """
        Finds the highest score, then finds which player(s) have that score,
        and reports them as the winner.
        """
        winners = []
        try:
            win_score = max(self.scores.values())
            for key in self.scores.keys():
                if self.scores[key] == win_score:
                    winners.append(key)
                else:
                    pass
            winstring = " & ".join(winners)
            print("And the winner is...{}!".format(winstring))
        except ValueError:
            print("everyone lost!")

    def hit(self, player):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        new_card = self.deck.draw()
        player.hand.append(newcard)
        print("   Drew the {}.".format(str(new_card)))

    def play(self, player):
        """
        An individual player's turn.
        """
        while True:
            points = sum_hand(player.hand)

            if points < 18:
                print("  hit")
                self.hit(player)
            elif points == 21:
                print("   {} wins!".format(player.name))
                sys.exit(0) # End if someone wins
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 
                print("   Standing at {} points.".format(str(points)))
                self.scores[player.name] = points
                break

def hand(hand: list):
    """
    Converts cards into point values for for score
    """
    x = [card.rank for card in hand]
    intervals = []
    while len(vals) > 0:
        val = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if val in ['K', 'Q', 'J']:
                intvals.append(10)
            elif value == 'A':
                intvals.append(1)  
    if intervals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intervals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("bob"), Player("ali"), Player("donald"),
        Player("justin")])
    game.blackjack()

