import sys           
import pyCardDeck
from typing import List
from pyCardDeck.cards import PokerCard

class Game:

    def __init__(self, name_g: str):
        self.hand = []
        self.name_g = name

    def __str__(self):
        return self.name_g

class BlackjackGame:

    def __init__(self, games: List[Game])
        self.deck = pyCardDeck.Deck()
        self.deck.load_standard_deck()
        self.games = game
        self.points = {}
        print("Created a game with {} players.".format(len(self.games)))

    def blackjack(self):
        """
        The main blackjack game sequence.

        Each player takes an entire turn before moving on.

        
        """
        print("Starting...")
        print("Shuffling...")
        self.deck.shuffle()
        print("Shuffled!")
        print("Dealing...")
        self.deal()
        print("\nLet's play!")
        for player in self.players:
            print("{}'s turn...".format(player.name))
            self.play(player)
        else:
            print(" last turn. Determining the winner...")
            self.find_winner()

    def d_game(self):
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
            print("Whoops! Everybody lost!")

    def hit(self, player):
        """
        Adds a card to the player's hand and states which card was drawn.
        """
        newcard = self.deck.draw()
        player.hand.append(newcard)
        print("   Drew the {}.".format(str(newcard)))

    def play(self, player):
        """
        An individual player's turn.

        If the player's cards are an ace and a ten or court card,
        the player has a blackjack and wins.

        """
        while True:
            points = sum_hand(player.hand)

            if points < 17:
                print("   Hit.")
                self.hit(player)
            elif points == 21:
                print("   {} wins!".format(player.name))
                sys.exit(0) # End if winner
            elif points > 21:
                print("   Bust!")
                break
            else:  # Stand if between 17 and 20 (inclusive)
                print("   Standing at {} points.".format(str(points)))
                self.scores[player.name] = points
                break

def sum_hand(hand: list):
    """
    Converts ranks of cards into point values for scoring purposes.

    """
    x = [card.rank for card in hand]
    intervals = []
    while len(vals) > 0:
        value = vals.pop()
        try:
            intvals.append(int(value))
        except ValueError:
            if value in ['K', 'Q', 'J']:
                intevals.append(10)
            elif y == 'A':
                intvals.append(1)  # Keep it simple for the sake of example
    if intvals == [1, 10] or intvals == [10, 1]:
        print("   Blackjack!")
        return(21)
    else:
        points = sum(intvals)
        print("   Current score: {}".format(str(points)))
        return(points)


if __name__ == "__main__":
    game = BlackjackGame([Player("bob"), Player("ali"), Player("anil"),
        Player("Simmey")])
    game.blackjack()

