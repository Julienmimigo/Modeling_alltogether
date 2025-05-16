from creation_of_deck import Deck, Card

class Hand:
    """
    A class representing a poker hand consisting of 5 cards drawn from a deck.
    Includes properties to evaluate different poker combinations (e.g., flush, pair, straight).
    """

    def __init__(self, deck):
        """
        Initializes a new hand by dealing 5 cards from the given deck.

        Parameters:
            deck (Deck): A deck object to deal cards from.
        """
        self._cards = [deck.deal() for _ in range(5)]

    @property
    def cards(self):
        """Returns the list of 5 cards in the hand."""
        return self._cards

    def __str__(self):
        """Returns a string representation of the hand."""
        return str(self.cards)

    @property
    def is_flush(self):
        """
        Checks if the hand is a flush (all cards have the same suit).

        Returns:
            bool: True if all cards have the same suit, False otherwise.
        """
        first_suit = self.cards[0].suit
        return all(card.suit == first_suit for card in self.cards)

    @property
    def num_matches(self):
        """
        Counts the number of rank matches in the hand.
        (Each pair contributes 2 to the count.)

        Returns:
            int: Total number of matching rank pairs.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i != j and self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """
        Checks if the hand contains exactly one pair.

        Returns:
            bool: True if the hand has one pair, False otherwise.
        """
        return self.num_matches == 2

    @property
    def is_2pair(self):
        """
        Checks if the hand contains exactly two different pairs.

        Returns:
            bool: True if the hand has two pairs, False otherwise.
        """
        return self.num_matches == 4

    @property
    def is_trips(self):
        """
        Checks if the hand contains three cards of the same rank.

        Returns:
            bool: True if the hand has a three-of-a-kind, False otherwise.
        """
        return self.num_matches == 6

    @property
    def is_quads(self):
        """
        Checks if the hand contains four cards of the same rank.

        Returns:
            bool: True if the hand has four-of-a-kind, False otherwise.
        """
        return self.num_matches == 12

    @property
    def is_full_house(self):
        """
        Checks if the hand is a full house (three-of-a-kind + one pair).

        Returns:
            bool: True if the hand is a full house, False otherwise.
        """
        return self.num_matches == 8

    @property
    def is_straight(self):
        """
        Checks if the hand is a straight (five cards in sequential rank order).
        A straight:
          - Must have no duplicate ranks (num_matches == 0)
          - The difference between highest and lowest card ranks must be 4

        Returns:
            bool: True if the hand is a straight, False otherwise.
        """
        sorted_cards = sorted(self.cards)  # Don't mutate self._cards
        high = Card.RANKS.index(sorted_cards[4].rank)
        low = Card.RANKS.index(sorted_cards[0].rank)
        return self.num_matches == 0 and high - low == 4


# --- Simulation: Estimate probability of being dealt a straight ---

matches = 0
trials = 0

while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    trials += 1

    if hand.is_straight:
        matches += 1

estimated_probability = 100 * matches / trials
print(f"The estimated probability of getting a straight is {estimated_probability:.4f}%")


#---Simulation: Estimate probability of being dealt a full house
matches = 0
trials = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = Hand(deck)
    trials += 1

    if hand.is_full_house:
        matches += 1

estimated_probability = 100 * matches / trials
print(f"The estimated probability of getting a full house is {estimated_probability:.4f}%")