#---------------------------
#      14/10/2017
# created by Wojciech Kuczer 
#---------------------------

import game, cards

class BJ_Card(cards.Card):
    """Black Jack card"""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """Deck of cards required to plaj BJ"""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    """BJ hand"""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + "\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        #addin cards value
        t = 0
        for card in self.cards:
            t += card.value

        #find out if ace is present
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        #if ace is present and total is lower than 11
        #treat ace as 11
        if contains_ace and t <= 11:
            t += 10

        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand):
    """Player"""
    def is_hitting(self):
        response = game.ask_yes_no("\n" + self.name + ", would you like another card? (Y/N)")
        return response == "Y"

    def bust(self):
        print(self.name, " is out")
        self.lose()

    def lose(self):
        print(self.name, " lost")

    def win(self):
        print(self.name, " wins")

    def push(self):
        print(self.name, " ties")

class BJ_Dealer(BJ_Hand):
    """BJ dealer"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, " is out")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game(object):
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additionl_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        """give 2 cards to each player"""
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        #give players additional cards
        for player in self.players:
            self.__additionl_cards(player)

        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additionl_cards(self.dealer)

            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                #compare point of players which still plaing
                for player in  self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

            #clear all cards
            for player in self.players:
                player.clear()
            self.dealer.clear()


def main():
    print("\t\tWelcome in Black Jack Game")

    names = []
    number = game.ask_number("Enter number of players (1 - 7)", 1, 8)
    for i in range(number):
        name = input("Enter players name:")
        names.append(name)
    print()

    gameBJ = BJ_Game(names)

    again = None
    while again != "N":
        gameBJ.play()
        again = game.ask_yes_no("\nDo You want to play again? (Y/N): ")


main()
input("\nTo Quit press Enter")














