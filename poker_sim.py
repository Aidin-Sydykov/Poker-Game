"""
author Aidin Sydykov
"""

from deck import Deck
from poker_hand import PokerHand

def play_game():
    """
    Runs the poker comparison game.

    It deals 5 card from the deck
    shows both hands
    asks the user to guess which hand is worth more
    compares it using compare_to
    tells if their guess is correct or not

    game goes on until there are less than 10 cards left in the deck
    """

    deck = Deck()
    deck.shuffle()

    while deck.size() >= 10:

        hand1_cards = [deck.deal() for i in range(5)]
        hand1 = PokerHand(hand1_cards)

        hand2_cards = [deck.deal() for j in range(5)]
        hand2 = PokerHand(hand2_cards)

        print("\nHand 1:")
        print(hand1)

        print("\nHand 2:")
        print(hand2)

        guess = input("\nWho wins? (1, 2, or tie): ")

        result = hand1.compare_to(hand2)

        if result > 0:
            correct = "1"
        elif result < 0:
            correct = "2"
        else:
            correct = "tie"

        if guess == correct:
            print("Correct!\n")
        else:
            print(f"Incorrect. Correct answer: {correct}\n")

    print("Not enough cards left to continue.")


if __name__ == "__main__":
    play_game()