"""
author Aidin Sydykov
"""

class Card:
    """
    Class representing a single playing card

    rank is the rank of the card (1-10/J/Q/K/A)
    suit is the suit of the card
    """
    def __init__(self, rank, suit):
        """
        Creates a new Card object
        """
        self._card = {"rank": rank, "suit": suit}

    def get_rank(self):
        """
        returns the rank of the card
        """
        return self._card["rank"]
    
    def get_suit(self):
        """
        returns the suit of the card
        """
        return self._card["suit"]
    
    def __str__(self):
        """
        returns a string of the card 
        """
        rank_names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

        rank = self.get_rank()

        suit_names = {"H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"}

        rank_str = rank_names.get(rank, str(rank))
        suit_str = suit_names[self.get_suit()]

        return f"{rank_str} of {suit_str}"