import random

class Card:
    """
    A class representing a standard playing card with a rank and a suit.
    Provides support for comparison based on rank and clean string representations.
    """

    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]  # Clubs, Diamonds, Hearts, Spades

    def __init__(self, rank, suit):
        """
        Initializes a Card instance after validating the given rank and suit.

        Parameters:
            rank (str): The rank of the card, e.g., 'A', '10', 'J'.
            suit (str): The suit symbol, e.g., '♠'.

        Raises:
            ValueError: If rank or suit is invalid (not found in RANKS or SUITS).
        """
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank '{rank}'. Must be one of: {self.RANKS}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit '{suit}'. Must be one of: {self.SUITS}")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """Returns the rank of the card."""
        return self._rank

    @property
    def suit(self):
        """Returns the suit of the card."""
        return self._suit

    def __str__(self):
        """
        Returns a string representation of the card (rank followed by suit).

        Returns:
            str: A readable format of the card, e.g., 'A♠'.
        """
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """
        Returns the official string representation for the card object.
        Useful for printing inside containers like lists.

        Returns:
            str: String format as returned by __str__.
        """
        return self.__str__()

    def __eq__(self, other):
        """
        Determines equality of two cards based on their rank.

        Parameters:
            other (Card): The other card to compare with.

        Returns:
            bool: True if ranks are equal, False otherwise.
        """
        return self.rank == other.rank

    def __lt__(self, other):
        """
        Compares two cards using their rank positions in the RANKS list.

        Parameters:
            other (Card): The other card to compare with.

        Returns:
            bool: True if self's rank is less than other's.
        """
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

    def __gt__(self, other):
        """
        Compares two cards using their rank positions in the RANKS list.

        Parameters:
            other (Card): The other card to compare with.

        Returns:
            bool: True if self's rank is greater than other's.
        """
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)


class Deck:
    """
    A class representing a standard deck of 52 playing cards.
    Provides methods for shuffling and dealing cards.
    """

    def __init__(self):
        """
        Initializes the deck by creating all 52 card combinations (one of each rank and suit).
        Stores them in a private list attribute.
        """
        self._cards = [Card(rank, suit) for suit in Card.SUITS for rank in Card.RANKS]

    @property
    def cards(self):
        """Provides read-only access to the list of cards."""
        return self._cards

    def __str__(self):
        """
        Returns a string representation of the entire deck.

        Returns:
            str: List of cards in the deck in current order.
        """
        return str(self._cards)

    def shuffle(self):
        """
        Randomly shuffles the order of cards in the deck.

        Returns:
            None
        """
        random.shuffle(self._cards)

    def deal(self):
        """
        Removes and returns the top card of the deck (first in list).

        Returns:
            Card: The card at the top of the deck.
        """
        return self._cards.pop(0)


# --- Example usage for testing and demonstration ---

if __name__ == "__main__":
    # Create a single card
    ace_of_spades = Card("A", "♠")
    print("Created card:", ace_of_spades)
    print("Suit:", ace_of_spades.suit, "| Rank:", ace_of_spades.rank)

    # Create a deck and display it
    deck = Deck()
    print("\nInitial deck:")
    print(deck)

    # Shuffle the deck
    deck.shuffle()
    print("\nShuffled deck:")
    print(deck)

    # Deal the top card
    top_card = deck.deal()
    print("\nDealt top card:", top_card)
    print("\nDeck after dealing one card:")
    print(deck)