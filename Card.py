# Learning to use python in everyday life 

import collections
import random

# Define the card data structure 
Card = collections.namedtuple('Card', ['rank', 'suit'])

# Define suits and ranks
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
suits = list(suit_values.keys())
ranks = [str(n) for n in range(2, 11)] + list('JQKA')

# Generate a full deck of cards 

all_cards = [Card(rank, suit) for rank in ranks for suit in suits]
class FrenchDeck:
    
    def __init__(self, cards):
        self._cards = cards

    def __len__(self):
        return len(self._cards)
    
    def __str__(self):
        return '\n'.join(str(card) for card in self._cards)
    
    def shuffle(self):
        random.shuffle(self._cards)

    def draw_card(self):
        return self._cards.pop() if self._cards else None
    
# Main function to test the deck

def main():

    deck = FrenchDeck(all_cards.copy()) # make a copy to avoid modfying the main data
    print(f"total cards in the deck : {len(deck)}")

    print("Shuffling the deck")
    deck.shuffle()

    print("Top 5 cards from the shuffled deck:")
    # for i in range(5):
    #     print(deck.draw_card())

    print(deck)


if __name__ == '__main__':
    main()
