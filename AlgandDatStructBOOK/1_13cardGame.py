from random import shuffle

class Card:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = [None, None,"2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]

    def __init__(self, v, s):
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit

    def __hash__(self):
        return hash(self.values[self.value] + " of " + self.suits[self.suit])    


class Deck(Card):
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
     

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.hand = []
        self.name = name

    def play_card(self):
        if len(self.hand) == 0:
            return
        return self.hand.pop()

class Pile:
    def __init__(self):
        self.cards = []
    
    def peek(self):
        top = len(self.cards) - 1
        print(self.cards[top])



class Game:
    # Definition of picture cards held as set
    picture_cards = {Card(11, 0), Card(12, 0), Card(13, 0), Card(14, 0),\
                     Card(11, 1), Card(12, 1), Card(13, 1), Card(14, 1),\
                    Card(11, 2), Card(12, 2), Card(13, 2), Card(14, 2),\
                    Card(11, 3), Card(12, 3), Card(13, 3), Card(14, 3)}
    
    # Definition of Jack held as set
    jacks = {Card(11, 0), Card(11, 1), Card(11, 2), Card(11, 3)}

    # Definition of Queen held as set
    queens = {Card(12, 0), Card(12, 1), Card(12, 2), Card(12, 3)}

    # Definition of King held as set
    kings = {Card(13, 0), Card(13, 1), Card(13, 2), Card(13, 3)}

    # Definition of Ace held as set
    aces = {Card(14, 0), Card(14, 1), Card(14, 2), Card(14, 3)}

    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
       
        # Deal the cards to the two players
        # while len(self.deck.cards) > 0:
        #    self.p1.hand.append(self.deck.rm_card())
        #    self.p2.hand.append(self.deck.rm_card())

####################################################################################################################        
        
        # Create Test Hand One. All non picture cards in 2 suits (spades and hearts)
        
        #for i in range(2,11):
        #    self.p1.hand.append(Card(i, 0))
        #for j in range(2, 11):
        #    self.p2.hand.append(Card(j, 1))
        
        # Create Test Hand Two. All picture cards in 2 suits (spades and hearts)
        
        for i in range(11, 15):
            self.p1.hand.append(Card(i, 0))
        for j in range(11, 15):
            self.p2.hand.append(Card(j, 1))

        # Create Test Hand Three. One picture card for p1 (Jack of spades). All non-picture cards for p2(hearts).
        
        #self.p1.hand.append(Card(11, 0))
        #for i in range(2, 11):
        #    self.p2.hand.append(Card(i, 1))

        # Create Test Hand Four. One picture card for p1 (Jack of spades) plus set of non-picture cards (spades).
        # One picture card for p2 (Jack of hearts) plus set of non-picture cards (hearts).
        
        #for i in range(2, 11):
        #    self.p1.hand.append(Card(i, 0))
        #self.p1.hand.append(Card(11, 0))

        #for j in range(2, 11):
        #    self.p2.hand.append(Card(j, 1))
        #self.p2.hand.append(Card(11, 1))

###########################################################################################################################
        
        # Create empty pile of cards
        self.pile = Pile()

    # When a round is won the winner picks up all cards in the pile and adds to back of hand  
    def collect(self, player):
        '''player parameter is self.p1 or self.p2'''
        player.hand = self.pile.cards + player.hand


    def play_game(self):
        
        # cards = self.deck.cards
        print("beginning Strip Jack Naked!")
        card_p1 = self.p1.play_card()
    
        if card_p1 in self.aces:
            print("Card is Ace")
        
        card_p2 = self.p2.play_card()
        self.pile.cards.append(card_p1)
        self.pile.peek()
        self.pile.cards.append(card_p2)
        self.pile.peek()

        # self.collect(self.p1)

        # while len(h1 and h2) > 0:
        #    m = "q to quit. Any " + \
        #        "key to play:"
        #    response = input(m)
        #    if response == 'q':
        #        break
        #p1c = self.hand1.rm_card()
        #p2c = self.hand2.rm_card()



# Need hand = deck.split (splits deck into two hands one for each player)
# 
# Need to draw card from first hand if 2 - 10, other player draws a card
# if picture card: Jack, Queen, King, Ace other player draws a card and keeps
# drawing until they draw a picture card or has drawn max cards: ( Ace: 4, King: 3, Queen: 2, Jack: 1)
# if reach max cards then oppposing player picks up 'pool' of cards. (Need list of pool cards). 
# Pool of cards added to back of hand and restarts. Game ends when one player has no cards in hand.
#
# To think about:
# 1) create hand from deck.split, deal.
# 2) draw cards into pile of cards
# 3) logic of drawing cards and they being picture cards or 2-10
# 4) picking up pile of cards and adding to back of hand and restarts
# 5) game end.        

#c1 = Card(2, 1)
#print (c1)

#d1 = Deck()
# crd1 = d1.rm_card
#print(d1.rm_card())

g1 = Game()

print(g1.p1.name)
print (g1.p1.hand)

print(g1.p2.name)
print(g1.p2.hand)

g1.play_game()

#print(g1.p1.name)
#print(g1.p1.hand)