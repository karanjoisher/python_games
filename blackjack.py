############### Karan Joisher ##################

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")
CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False # Keeps track of whether the player's round is over or not
outcome = ""    # Stores messages that are displayed on the canvas to appeal certain action from player
score = 0       # Keeps track of the current score

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class ------------------------------------------------------------------------------------------------------------
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
        
# define hand class -----------------------------------------------------------------------------------------------------------
class Hand:
    def __init__(self):
        self.cards = []  # A list of cards that contains all the cards in a particular hand (dealer or player)

    def __str__(self):
        
        ''' Returns a string which contains all the cards present in the hand.
        
        >>>str(player_hand)
        Hand contains SA C2 DT
        
        '''
        hand = ''
        for card in self.cards:
            hand += str(card) + ' '
        return 'Hand contains ' + hand 
    
    def add_card(self, card):
        
        ''' Adds card(a Card object) to the Hand object
        
        >>>player_hand.add_card(Card("D", "T"))
        >>>str(player_hand)
        Hand contains DT
        
        '''
        self.cards.append(card)	        
    
    def reset(self):
        'Resets the number of Card objects in Hand object to 0'
        self.cards = []
    
    def get_value(self):
        ''' Computes the value of each Card object in the Hand object and thus returns the value of Hand object
        
        Initially it would iterate over each Card object and add the corresponding value from VALUES dictionary to the 
        global variable value.If an ace is encountered during this process the aces counter increases by 1 and it's value
        is taken as 1 then added to value variable. After each Card object has been iterated another while loop is created
        which remains true till number of aces become 0. If taking the value of ace as 11 doesn't make the value variable
        greater than 21, then 10 is added to value.Else no change is done.
        
        '''
        value = 0
        aces = 0
        for card in self.cards:	
            if (card.get_rank() == 'A'):
               aces += 1
               value += 1
            else:
                value += VALUES[card.get_rank()]
        while aces > 0:
            if ((value + 10) <= 21):
                    value += 10
            aces -= 1
            
        return value
                
    def draw(self, canvas, pos):
        ' Iterates over each Card object and draws it '
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + i * 75 , pos[1]])
            
# define deck class----------------------------------------------------------------------------------------------------------- 
class Deck:
    def __init__(self):
        ' Creates a deck with all cards present in it '
        self.deck = []
        for suit in SUITS:	
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)
                
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck) 
    
    def restock(self):
        ''' Restores all the cards '''
        self.__init__()
    
    def deal_card(self):
        ' Deals out a card '
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        deck_cards = ''
        for card in self.deck:	# return a string representing the deck
            deck_cards += str(card) + ' '
        return 'Deck contains ' + deck_cards

#define event handlers for buttons ------------------------------------------------------------------------------------------
def deal():
    global outcome, in_play, deck, score
    
    # Intializing objects for a new deal
    player_hand.reset()
    dealer_hand.reset() 
    deck.restock()
    
    # Shuffles the deck and deals out two cards to both player as well as dealer
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    outcome = 'Hit or stand?'
    
    # Checks whether the player hits the deal button in between an ongoing game.If so reduces the score by 1
    if in_play:
        score -= 1
    in_play = True
    
#---------------------------------------------------------------------------------------------------------------------------    
    
def hit():
    global in_play, outcome, score
    if in_play:
        # Deals a card to the player if the player is not already busted 
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
        # Checks whether player is busted or not    
        if player_hand.get_value() > 21:
            outcome = 'You are busted!  New deal?'
            score -= 1
            in_play = False

# --------------------------------------------------------------------------------------------------------------------------            
def stand():
    global in_play, score, outcome
    if in_play:
        # Deal cards to the dealer as long as the value of dealer's hand is less than 17
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        
        # Checks whether dealer is busted or not
        if (dealer_hand.get_value() > 21):
            outcome = 'Dealer is busted! New deal?'
            score += 1
            in_play = False
            
        # If not busted than sees who is the winner of the round    
        elif (dealer_hand.get_value() < player_hand.get_value()):
            outcome = 'You win the hand. New deal?'
            score += 1
            in_play = False
        else:
            score -= 1
            outcome = 'Dealer wins the hand. New deal?'
            in_play = False
        
# draw handler ------------------------------------------------------------------------------------------------------------    
def draw(canvas):
    player_hand.draw(canvas, [0, 300]) # player's hand
    dealer_hand.draw(canvas, [0, 100]) # dealer's hand
    canvas.draw_text('Blackjack', [220, 30], 35, 'Black') # Title blackjack
    canvas.draw_text('Dealer', [0, 90], 35, 'Blue') 
    canvas.draw_text('Player', [0, 290], 35, 'Red')
    canvas.draw_text('Score: ' + str(score),[150, 290], 35, 'Purple') # Score
    canvas.draw_text(outcome, [0, 450], 35, 'Orange') # Instructions
    
    # If the player's turn is over then reveal's the dealer's hole card
    if in_play:
        canvas.draw_image(card_back, (71 / 2.0, 96 / 2.0), (71, 96), (36.5,149), (71, 96))

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
deck = Deck()
player_hand = Hand() # creating Hand object
dealer_hand = Hand() # creating Hand object
deal() # Start's a deal
frame.start()