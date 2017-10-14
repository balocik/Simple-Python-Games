#---------------------------
#      14/10/2017
# created by Wojciech Kuczer 
#---------------------------

class Card(object):
    """Card to play"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand(object):
    """All the cards"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def give_card(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add_card(card)


class Deck(Hand):
    """Deck of cards"""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add_card(Card(rank, suit))


    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for round in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give_card(top_card, hand)
                else:
                    print("No cards left in deck")

if __name__ == "__main__":
    print("You shouldn't use this modul directly.Import it please")
    input("\n\nPress Enter to Finish")















