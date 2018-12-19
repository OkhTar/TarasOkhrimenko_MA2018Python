# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

wins = 0
losses = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0

    def __str__(self):
        tmp = "hand contains "
        for card in self.cards:
            tmp += str(card) + " "
        return tmp   

    def add_card(self, card):
        self.cards.append(card)
        self.value += VALUES[card.rank]

    def get_value(self):
        a = [card for card in self.cards if card.get_rank() != 'A']
        self.value = 0
        for card in a:
            self.value += VALUES[card.get_rank()]
        if len(a) == len(self.cards):
            return self.value
        else:
            if self.value < 12:
                if self.value == 10 and (len(self.cards)-len(a)) == 2:
                    return 12
                for i in range(len(self.cards)-len(a)):
                    if self.value + 11 <= 21:
                        self.value += 11
                    else:
                        self.value += 1
                return self.value
            else:
                for i in range(len(self.cards)-len(a)):
                    self.value += 1
                return self.value            
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.cards:
            card.draw(canvas,[pos[0]+i*100,pos[1]])
            i += 1
            
            
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit,rank))
        random.shuffle(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        tmp = "Deck contains "
        for card in self.cards:
            tmp += str(card) + " "
        return tmp



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, score, wins, losses

    if in_play == True:
        outcome = "Foul play. Dealer wins"
        in_play = False
        losses += 1
    else:
        deck = Deck()
        dealer.cards = []
        player.cards = []
        
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())        
        
        # console log
        # VALUE displayed only for debug, must be remove in real game
        print "===========START==========="
        print "Dealer " + str(dealer) + "(VALUE: " + str(dealer.get_value()) + ")"
        print "Player " + str(player) + "(VALUE: " + str(player.get_value()) + ")"

        in_play = True

def hit():
    global outcome, in_play, score, wins, losses
    
    if in_play == True:
        player.add_card(deck.deal_card())
        print "Player " + str(player) + "(VALUE: " + str(player.get_value()) + ")"

        
        if player.get_value() > 21 and in_play == True:
            outcome = "You have busted. Dealer wins"
            in_play = False
            losses += 1
            
def stand():
    global outcome, in_play, score, wins, losses
    
    if in_play == True and dealer.get_value() < 18:
        while dealer.get_value() < 18:
            dealer.add_card(deck.deal_card())
        print "Dealer new " + str(dealer) + "(VALUE: " + str(dealer.get_value()) + ")"
        stand()
    elif in_play == True and dealer.get_value() > 21:
        outcome = "Dealer busted, YOU WIN!"
        in_play = False
        wins += 1
    elif in_play == True and player.get_value() < dealer.get_value():
        outcome = "Dealer wins!"
        in_play = False
        losses += 1
    elif in_play == True and player.get_value() == dealer.get_value():
        outcome = "Tie!"
        in_play = False
    elif in_play == True:
        outcome = "YOU WIN!"
        in_play = False
        wins += 1
        


        
# draw handler    
def draw(canvas):
    global wins, losses
   
    player.draw(canvas, [50,400])
    dealer.draw(canvas, [50,200])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50+36.5,200+49], CARD_BACK_SIZE)
    else:
        canvas.draw_text("New Deal?", [150, 350], 28, "Black")
        canvas.draw_text(outcome, [150, 100], 32, "Blue")
        
    canvas.draw_text("Blackjack", [50, 50], 36, "White")
    canvas.draw_text("Dealer", [50, 190], 28, "Black")
    canvas.draw_text("Player", [50, 390], 28, "Black")
    canvas.draw_text("Wins: " + str(wins), [250, 50], 28, "Maroon")
    canvas.draw_text("Losses: " + str(losses), [450, 50], 28, "Maroon")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
dealer = Hand()
player = Hand()

deck = Deck()
deal()
frame.start()


# remember to review the gradic rubric
