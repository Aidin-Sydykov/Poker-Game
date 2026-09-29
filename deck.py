"""
author Aidin Sydykov
"""

import random
from card import Card

class Deck:
    """
    Class for 52 card deck
    """

    def __init__(self):
        """
        Creates shuffled 52 card deck
        """
        self._cards = []
        self._create_deck()
        self.shuffle()

    def _create_deck(self):
        """
        Creates a standard 52 card deck
        """
        self._cards = []
        for rank in range(2, 15):
            for suit in ["H", "D", "S", "C"]:
                self._cards.append(Card(rank, suit))

    def shuffle(self):
        """
        Shuffles the deck
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Removes and returns top of deck
        """
        if self.size() == 0:
            return None
        return self._cards.pop()
    
    def size(self):
        """
        Returns amount of cards
        """
        return len(self._cards)
    
    def __str__(self):
        """
        Returns string of all remaining cards
        """
        result = ""
        for i in range(len(self._card)):
            result += str(self._cards[i])
            if i < len(self._cards) - 1:
                result += "\n"
        return result