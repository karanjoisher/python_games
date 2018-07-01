import simplegui, random

WIDTH = 600
HEIGHT = 630
ball_radius = 20
height_s = 70
width_s = 100
down = height_s
up = - height_s
right = width_s
left = - width_s
winning_player = 0
winning_color = ''
properties = {11: [[],'', [right, down]],
              12: [[],'', [right, up,  down]],
              13: [[],'', [right, up, down]],
              14: [[],'', [right, up,  down]],
              15: [[],'', [right, up, down]],
              16: [[],'', [right, up, down]],
              17: [[],'', [right, up,  down]],
              18: [[],'', [right, up, down]],
              19: [[],'', [right, up]],
              21: [[],'', [right, down, left]],
              22: [[],'', [left, up, right, down]],
              23: [[],'', [left, up, right, down]],
              24: [[],'', [left, up, right, down]],
              25: [[],'', [left, up, right, down]],
              26: [[],'', [left, up, right, down]],    
              27: [[],'', [left, up, right, down]],
              28: [[],'', [left, up, right, down]],
              29: [[],'', [right, up, left]],
              31: [[],'', [left, down, right]],
              32: [[],'', [left, up, right, down]],
              33: [[],'', [left, up, right, down]],
              34: [[],'', [left, up, right, down]],
              35: [[],'', [left, up, right, down]],
              36: [[],'', [left, up, right, down]],
              37: [[],'', [left, up, right, down]],
              38: [[],'', [left, up, right, down]],
              39: [[],'', [right, up, left]],
              41: [[],'', [left, down, right]],
              42: [[],'', [left, up, right, down]],
              43: [[],'', [left, up, right, down]],
              44: [[],'', [left, up, right, down]],
              45: [[],'', [left, up, right, down]],
              46: [[],'', [left, up, right, down]],
              47: [[],'', [left, up, right, down]],
              48: [[],'', [left, up, right, down]],
              49: [[],'', [right, up, left]],
              51: [[],'', [left, down, right]],
              52: [[],'', [left, up, right, down]],
              53: [[],'', [left, up, right, down]],
              54: [[],'', [left, up, right, down]],
              55: [[],'', [left, up, right, down]],
              56: [[],'', [left, up, right, down]],
              57: [[],'', [left, up, right, down]],
              58: [[],'', [left, up, right, down]],
              59: [[],'', [right, up, left]],
              61: [[],'', [left, down]],
              62: [[],'', [left, up,  down]],
              63: [[],'', [left, up,  down]],
              64: [[],'', [left, up,  down]],
              65: [[],'', [left, up,  down]],
              66: [[],'', [left, up,  down]],
              67: [[],'', [left, up,  down]],
              68: [[],'', [left, up,  down]],
              69: [[],'', [left, up]]}

num_players = 0
color_list = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Gray', 'White']
players = []
turn = 0
win = False
first_time = True

def new_game():
    global winning_player, winning_color, properties, num_players, color_list, players, turn, win , first_time
    
    winning_color = ''
    properties = {11: [[],'', [right, down]],
              12: [[],'', [right, up,  down]],
              13: [[],'', [right, up, down]],
              14: [[],'', [right, up,  down]],
              15: [[],'', [right, up, down]],
              16: [[],'', [right, up, down]],
              17: [[],'', [right, up,  down]],
              18: [[],'', [right, up, down]],
              19: [[],'', [right, up]],
              21: [[],'', [right, down, left]],
              22: [[],'', [left, up, right, down]],
              23: [[],'', [left, up, right, down]],
              24: [[],'', [left, up, right, down]],
              25: [[],'', [left, up, right, down]],
              26: [[],'', [left, up, right, down]],    
              27: [[],'', [left, up, right, down]],
              28: [[],'', [left, up, right, down]],
              29: [[],'', [right, up, left]],
              31: [[],'', [left, down, right]],
              32: [[],'', [left, up, right, down]],
              33: [[],'', [left, up, right, down]],
              34: [[],'', [left, up, right, down]],
              35: [[],'', [left, up, right, down]],
              36: [[],'', [left, up, right, down]],
              37: [[],'', [left, up, right, down]],
              38: [[],'', [left, up, right, down]],
              39: [[],'', [right, up, left]],
              41: [[],'', [left, down, right]],
              42: [[],'', [left, up, right, down]],
              43: [[],'', [left, up, right, down]],
              44: [[],'', [left, up, right, down]],
              45: [[],'', [left, up, right, down]],
              46: [[],'', [left, up, right, down]],
              47: [[],'', [left, up, right, down]],
              48: [[],'', [left, up, right, down]],
              49: [[],'', [right, up, left]],
              51: [[],'', [left, down, right]],
              52: [[],'', [left, up, right, down]],
              53: [[],'', [left, up, right, down]],
              54: [[],'', [left, up, right, down]],
              55: [[],'', [left, up, right, down]],
              56: [[],'', [left, up, right, down]],
              57: [[],'', [left, up, right, down]],
              58: [[],'', [left, up, right, down]],
              59: [[],'', [right, up, left]],
              61: [[],'', [left, down]],
              62: [[],'', [left, up,  down]],
              63: [[],'', [left, up,  down]],
              64: [[],'', [left, up,  down]],
              65: [[],'', [left, up,  down]],
              66: [[],'', [left, up,  down]],
              67: [[],'', [left, up,  down]],
              68: [[],'', [left, up,  down]],
              69: [[],'', [left, up]]}

    num_players = 0
    color_list = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Gray', 'White']
    players = []
    turn = 0
    win = False
    first_time = True
    


def key_atom(pos):
    return int((str(pos[0] // 100 + 1)) + (str(pos[1] // 70 + 1)))

def center(pos):
    center_x = (((pos[0] // 100) * 100) + ((pos[0] // 100 + 1) * 100)) // 2
    center_y = (((pos[1] // 70) * 70) + ((pos[1] // 70 + 1) * 70)) // 2 
    return [center_x, center_y]
    
def keys_crossing_limit():
    excess = []
    for key in properties:
        if len(properties[key][0]) >= len(properties[key][-1]):
            excess.append(key)
    return excess
    
def scattering_atoms(list_keys):
    global players, properties
    counter = 0
    for key in list_keys:
        for i in range(len(properties[key][0])):
            if (key // 10 == 1 or key // 10 == 6) and (not(key % 10 in [1, 9])):
                if counter == 0:
                    properties[key][0][i][0] += properties[key][-1][i]
                elif counter == 1:
                    properties[key][0][i][1] += properties[key][-1][i]
                elif counter == 2:
                    properties[key][0][i][1] += properties[key][-1][i]
                counter += 1
                properties[key_atom(properties[key][0][i])][0].append(properties[key][0][i])
                
                properties[key_atom(properties[key][0][i])][1] = players[turn] 
                
            else:
                properties[key][0][i][i % 2] += properties[key][-1][i]
                properties[key_atom(properties[key][0][i])][0].append(properties[key][0][i])
                
                properties[key_atom(properties[key][0][i])][1] = players[turn]
        properties[key][0] = []
        properties[key][1] = ''
   
def creating_atoms(pos):
    global players, properties
    properties[key_atom(pos)][0].append(pos)
    properties[key_atom(pos)][1] = players[turn]
    
    
def select_players(num):
    global num_players, players
    if 2 <= int(num) <= 8:
        num_players = int(num)
        for i in range(num_players):
            players.append(color_list[i])
        num_players = len(players)

    #print players
    #print num_players
    
def winner():
    global winning_color
    in_play = []
    global first_time, win, total_balls
    if not(first_time):
        in_play = [properties[key][1] for key in properties if properties[key][1] != '']
        for i in range(1, len(in_play)):
            if (in_play[i - 1] == in_play[i]):
                win = True 
            else:
                win = False
                break
        if win:
            for color in players:
                if color == in_play[0]:
                    winning_color = color
                    
 
def update_play():
    global turn
    print 'eneterd'
    not_on_board = []
    to_be_removed = ''
    if not(first_time):
        for color in players:
            for key in properties:
                if properties[key][1] != color:
                    to_be_removed = color 
                else:
                    to_be_removed = ''
                    break
            if to_be_removed != '':
                not_on_board.append(to_be_removed)
        print not_on_board        
        if not_on_board !=  []:
            for i in not_on_board:
                players.remove(i)
        if turn >= len(players):
            turn = 0
        
                    


                    
def click(pos):
    global players, turn, num_players, winner, first_time
    num_players = len(players)
    if turn >= len(players):
        turn = 0
    print turn
    #print players
    if not(win):
        if ((properties[key_atom(pos)][1] == players[turn]) or (len(properties[key_atom(pos)][1]) == 0)) and num_players >= 2:
            update_play()
            pos = list(pos)
            creating_atoms(pos)
            while len(keys_crossing_limit()) > 0:
                scattering_atoms(keys_crossing_limit())
            turn += 1
            if turn == num_players:
                first_time = False
            winner()
            print turn
    #print properties
        
def draw(c):
    #columns
    c.draw_line([width_s, 0], [width_s, HEIGHT], 1, 'White')
    c.draw_line([width_s * 2, 0], [width_s * 2, HEIGHT], 1, 'White')
    c.draw_line([width_s * 3, 0], [width_s * 3, HEIGHT], 1, 'White')
    c.draw_line([width_s * 4, 0], [width_s * 4, HEIGHT], 1, 'White')
    c.draw_line([width_s * 5, 0], [width_s * 5, HEIGHT], 1, 'White')
    
    #rows
    c.draw_line([0, height_s], [WIDTH, height_s], 1, 'White')
    c.draw_line([0, height_s * 2], [WIDTH, height_s * 2], 1, 'White')
    c.draw_line([0, height_s * 3], [WIDTH, height_s * 3], 1, 'White')
    c.draw_line([0, height_s * 4], [WIDTH, height_s * 4], 1, 'White')
    c.draw_line([0, height_s * 5], [WIDTH, height_s * 5], 1, 'White')
    c.draw_line([0, height_s * 6], [WIDTH, height_s * 6], 1, 'White')
    c.draw_line([0, height_s * 7], [WIDTH, height_s * 7], 1, 'White')
    c.draw_line([0, height_s * 8], [WIDTH, height_s * 8], 1, 'White')
    
    for keys in properties:
        for ball_index in range(len(properties[keys][0])):
            if len(properties[keys][0]) != 0:
                x = random.choice([1,-1])
                y = random.choice([1, -1])
                c.draw_circle([properties[keys][0][ball_index][0] + x,properties[keys][0][ball_index][1] + y] , ball_radius, 1, 'Yellow', properties[keys][1])
    if win:
        c.draw_line((0, 280), (WIDTH, 280), 140, 'Teal')
        c.draw_text(winning_color + ' wins', [20, 315], 100, winning_color )
        
frame = simplegui.create_frame('Chain Reaction', WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.add_input('Select number of players: 0 - 8', select_players,25)
frame.add_button('New game', new_game)
frame.start()