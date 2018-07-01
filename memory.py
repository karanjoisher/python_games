### Karan Joisher ###

import simplegui
import random

# Globals ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
state = 0                # Stores the state of game
                         # No cards revealed state = 0
                         # One card revealed state = 1
                         # 2 cards revealed state = 2

turns = 0                # Number of turns required to reveal all the cards
TURNS = 'Turns = ',turns # Used it for label
board = range(8) * 2     # board containing pairs of numbers ranging from 0 to but not including 8
exposed = [False] * 8	 # List of booleans that keeps track of whether the cards are revealed or not # False means they are not exposed # True means they are exposed
revealed_card1_index = 0 # Stores the index of first card revealed in each turn
revealed_card2_index = 0 # Stores the index of second card revealed in each turn



# helper function to initialize globals~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def new_game():
    'Sets all the global variables to their original value (Global section) and starts a new game'
    global state, turns, board, exposed, revealed_card1_index, revealed_card2_index
    random.shuffle(board)	                 # Shuffles the cards on board
    exposed = [False] * 16
    revealed_card1_index = 0
    revealed_card2_index = 0
    turns = 0
    state = 0
    label.set_text("Turns = " + str(turns))  # Updates label which displays number of turns
    
    
# define event handlers~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def mouseclick(pos):
    global state, exposed, revealed_card1_index, revealed_card2_index, turns
# State 0 -----------------------------------------------------------------------------------
    if state == 0: 
        for length in range(50, 850, 50):
            if (length - 50 <= pos[0] <= length) and exposed[(length / 50) - 1] == False:
                if turns > 0 and ((length / 50) - 1 == revealed_card1_index or (length / 50) - 1 == revealed_card2_index):
                    state = 0
                    break
                else:
                    if board[revealed_card1_index] != board[revealed_card2_index]:
                        exposed[revealed_card1_index] = False
                        exposed[revealed_card2_index] = False
                    state = 1
                    exposed[(length / 50) - 1] = True
                    revealed_card1_index = (length / 50) - 1
                    break
# State 1 ------------------------------------------------------------------------------------               
    elif state == 1:
        for length in range(50, 850, 50):
            if (length - 50 <= pos[0] <= length) and (exposed[(length / 50) - 1]) == False:
                exposed[(length / 50) - 1] = True
                revealed_card2_index = (length / 50) - 1
                state = 2
                turns += 1
                break
# State 2 --------------------------------------------------------------------------------------    
    elif state == 2:
        if board[revealed_card1_index] == board[revealed_card2_index]:
            exposed[revealed_card1_index] = True
            exposed[revealed_card2_index] = True
            state = 0
            mouseclick(pos)   
        else:
            state = 0
            mouseclick(pos)
                                   
# Draw handler ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    position_cards = [20, 65]
    position_rect = [[0, 0], [50, 0], [50, 100], [0,100]] 
    for i in range(len(board)):
        if exposed[i] == True:
            canvas.draw_text(str(board[i]), position_cards, 40, 'White')
        elif exposed[i] == False:
            canvas.draw_polygon(position_rect, 1, 'White', 'Green')
            
        position_cards[0] += 50
        for point in range(len(position_rect)):
            position_rect[point][0] += 50
    
    label.set_text("Turns = " + str(turns))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
#-----------------------------------------------------------------------------------------------------       
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

# create frame and add a button and labels

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()