"""
author Aidin Sydykov
"""

class PokerHand:
    """
    Represents 5 card poker hand
    """

    _HAND_VALUES = {"high card": 1, "pair": 2, "two pair": 3, "flush": 4}


    def __init__(self, cards):
        """
        Creates a pokerhand object
        """
        self._cards = list(cards)

    def add_card(self, card):
        """
        Add a card to the hand
        """
        self._cards.append(card)

    def get_ith_card(self, index):
        """
        returns card object at index
        """
        return self._cards[index]

    def __str__(self):
        """
        Returns a string representation of the hand
        """
        result = ""
        for i in range(len(self._cards)):
            result += str(self._cards[i])
            if i != len(self._cards) - 1:
                result += ", "
        return result

    def _is_flush(self):
        """
        Determines if all cards in the hand have the same suit.
        """
        first_suit = self._cards[0].get_suit()
        for card in self._cards:
            if card.get_suit() != first_suit:
                return False
        return True

    def _rank_counts(self):
            """
            Counts how many times each rank appears in the hand.
            """
            counts = {}
            for card in self._cards:
                rank = card.get_rank()
                if rank in counts:
                    counts[rank] += 1
                else:
                    counts[rank] = 1
            return counts

    def _hand_type(self):
            """
            Determines the type of poker hand.
            """
            if self._is_flush():
                return "flush"

            counts = self._rank_counts().values()

            num_pairs = 0
            has_three = False
            has_four = False

            for count in counts:
                if count == 4:
                    has_four = True
                elif count == 3:
                    has_three = True
                elif count == 2:
                    num_pairs += 1

            if has_four or (has_three and num_pairs == 1) or num_pairs == 2:
                return "two pair"

            if has_three or num_pairs == 1:
                return "pair"

            return "high card"

    def compare_to(self, other_hand):
        """
        Determines which hand is worth more 

        :param self: The first hand to compare
        :param other_hand: The second hand to compare
        :return: A negative number if self is worth less than other_hand,
                 zero if they are worth the same (a tie),
                 and a positive number if self is worth more than other_hand
        """
        self_type = self._hand_type()
        other_type = other_hand._hand_type()

        if self._HAND_VALUES[self_type] != self._HAND_VALUES[other_type]:
            return self._HAND_VALUES[self_type] - self._HAND_VALUES[other_type]

        self_ranks = [card.get_rank() for card in self._cards]
        other_ranks = [card.get_rank() for card in other_hand._cards]

        for i in range(len(self_ranks)):
            max_index = i
            for j in range(i + 1, len(self_ranks)):
                if self_ranks[j] > self_ranks[max_index]:
                    max_index = j

            temp = self_ranks[i]
            self_ranks[i] = self_ranks[max_index]
            self_ranks[max_index] = temp

        for i in range(len(other_ranks)):
            max_index = i
            for j in range(i + 1, len(other_ranks)):
                if other_ranks[j] > other_ranks[max_index]:
                    max_index = j

            temp = other_ranks[i]
            other_ranks[i] = other_ranks[max_index]
            other_ranks[max_index] = temp

        for i in range(len(self_ranks)):
            if self_ranks[i] != other_ranks[i]:
                return self_ranks[i] - other_ranks[i]

        return 0

