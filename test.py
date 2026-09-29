"""
author Aidin Sydykov
"""

from card import Card
from poker_hand import PokerHand


def test_compare():
    """
    Tests compares two pokerhand objects

    Creates two hands with pair aces and different high cards

    compares them using compare_to and checks if the result is correct
    then prints the hand, the result and if the test passed
    """

    hand1 = PokerHand([
        Card(14, "H"),
        Card(14, "D"),
        Card(7, "S"),
        Card(2, "C"),
        Card(9, "H")
    ])

    hand2 = PokerHand([
        Card(14, "S"),
        Card(14, "C"),
        Card(8, "D"),
        Card(4, "H"),
        Card(2, "S")
    ])

    result = hand1.compare_to(hand2)

    print("Hand 1:")
    print(hand1)
    print("\nHand 2:")
    print(hand2)

    print("\ncompare_to result:", result)

    if result > 0:
        print("Test passed.")
    else:
        print("Test failed.")


if __name__ == "__main__":
    test_compare()
