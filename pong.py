# ~~~~~~~~~~~~~~~~~~~~~~ KARAN JOISHER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import simplegui
import random

# GLOBALS ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
WIDTH = 600                         # Width of the canvas
HEIGHT = 400       					# Height of the canvas
BALL_RADIUS = 20					# Radius of the ball
PAD_WIDTH = 8						# Width of the paddles
PAD_HEIGHT = 80						# Height of the paddles 
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False						# Used when ball hits the gutter and then spawned in the opposite direction of the gutter
RIGHT = True						# Used when ball hits the gutter and then spawned in the opposite direction of the gutter
ball_pos = [WIDTH / 2, HEIGHT / 2]  # The position of centre of the ball on the canvas
ball_vel = [0, 0]					# Velocity with which the ball moves
paddle1_pos = 30 					# Y co-ordinate of the upper most part of the left paddle
paddle2_pos = 30					# Y co-ordinate of the upper most part of the right paddle 
paddle1_vel = 0						# Velocity with which the left paddle moves up and down (vertically)
paddle2_vel = 0						# Velocity with which the right paddle moves up and down (vertically)
velocity_increment = -5				# Increase in the velocity of paddles
left_player_score = 0				# Score of the player playing with left paddle
right_player_score = 0              # Score of the player playing with right paddle
right_color = 'White'				# Color of the player's score using right paddle
left_color = 'White'				# Color of the player's score using left paddle
ball_color = 'White'				# Color of the ball
first_time = True					# To check whether the game is being played for the first time


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]

    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240)/60.0 , -random.randrange(60, 180)/60.0] # Ball would go upwars and right
    elif direction  == LEFT:
        ball_vel = [-random.randrange(120, 240)/60.0, -random.randrange(60, 180)/60.0] # Ball would go upwars and left
        
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global left_player_score, right_player_score  # these are ints 
    left_player_score = 0 # resets the score
    right_player_score = 0 # resets the score
    ball_color = 'White'
    spawn_ball(random.choice([RIGHT,LEFT])) # Ball would get spawned in either left or right direction


def draw(c):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, up, velocity_increment, left_player_score, right_player_score, right_color, left_color, ball_color
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") # Right gutter
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") # Left gutter
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White") # Center line
    c.draw_circle([WIDTH / 2, HEIGHT / 2], 80, 1, 'White')    
    # update ball
    ball_pos[0] += ball_vel[0] # Incrementing X velocity
    ball_pos[1] += ball_vel[1] # Incrementing Y velocity
    
# ~~~~ Condition to check whether ball touches the upper or lower wall and then reflect it accordingly ~~~~~~~~~~~~
   
    
    if ball_pos[1] <= BALL_RADIUS: 
        ball_vel[0] = ball_vel[0] 
        ball_vel[1] = - ball_vel[1]
        #print ball_pos
    elif ball_pos[1] >= HEIGHT  - BALL_RADIUS: 
        ball_vel[0] = ball_vel[0]
        ball_vel[1] = - ball_vel[1]
        #print ball_pos

        
#~~~~~~ To check whether the ball hits the right paddle, if so then reflect it back or else spawn the ball towars the winner ~~~~~~~~~~         
    
    
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if paddle1_pos <= ball_pos[1] + BALL_RADIUS <= paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] + (10.0/100 * (-ball_vel[0]))
            ball_vel[1] = ball_vel[1] + (10.0/100 * ball_vel[1])
            ball_color = random.choice(['Aqua', 'Blue', 'Fuchsia', 'Gray', 'Maroon', 'Navy', 'Orange', 'Purple', 'Yellow', 'Silver'])
            #print ball_vel
        else:
            right_player_score += 1 
            spawn_ball(RIGHT)
            
            
#~~~~~~ To check whether the ball hits the left paddle, if so then reflect it back or else spawn the ball towars the winner ~~~~~~~~~~           
        
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if paddle2_pos <= ball_pos[1] + BALL_RADIUS <= paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] + (10.0/100 * (- ball_vel[0])) 
            ball_vel[1] = ball_vel[1] + (10.0/100 * ball_vel[1])
            ball_color = random.choice(['Aqua', 'Blue', 'Fuchsia', 'Gray', 'Maroon', 'Navy', 'Orange', 'Purple', 'Yellow', 'Silver'])
            #print ball_vel
        else:
            left_player_score += 1
            spawn_ball(LEFT)
            
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~            

    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 2, 'Black', ball_color)
    
    # update paddle's vertical position, keep paddle on the screen
    if 0 <= paddle1_pos + paddle1_vel <= 320:
        paddle1_pos += paddle1_vel
        
    if 0 <= paddle2_pos + paddle2_vel <= 320:
        paddle2_pos += paddle2_vel
        
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH , paddle1_pos], [HALF_PAD_WIDTH , paddle1_pos + PAD_HEIGHT], PAD_WIDTH, 'Yellow')
    c.draw_line([WIDTH - HALF_PAD_WIDTH , paddle2_pos], [WIDTH - HALF_PAD_WIDTH , paddle2_pos + PAD_HEIGHT], PAD_WIDTH, '#BF0033')
    
    # draw scores
    if right_player_score > left_player_score:
        right_color = 'Black'
        left_color = 'Red'
    elif right_player_score == left_player_score:
        right_color = 'White'
        left_color = 'White'
    else:
        right_color = 'Red'
        left_color = 'Black'
        
    # Score board ~~~~~~~~~~~~    
    c.draw_text(str(left_player_score), [WIDTH/4, HEIGHT/4], 30, left_color)
    c.draw_text(str(right_player_score), [WIDTH/2 + WIDTH/4, HEIGHT/4], 30, right_color)
    
    if first_time:
        c.draw_text('Hit spacebar to start playing!', [WIDTH - (WIDTH/2 + WIDTH/4), HEIGHT / 2 + HEIGHT/4], 30, 'Orange')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, velocity_increment, first_time
    # Controls for left paddle ~~~~~~~~~~~~~~~~~~~ 
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel += velocity_increment
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel -= velocity_increment
        
    # Controls for right paddle ~~~~~~~~~~~~~~~~~~~ 
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel += velocity_increment
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel -= velocity_increment
        
    if key == simplegui.KEY_MAP['space'] and first_time:
        first_time = False
        new_game()
   
def keyup(key):
    global paddle1_vel, paddle2_vel, velocity_increment
    # Controls for left paddle ~~~~~~~~~~~~~~~~~~~ 
    if key == simplegui.KEY_MAP['w'] or key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    
    # Controls for right paddle ~~~~~~~~~~~~~~~~~~~ 
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
        
# Restart button
def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', restart, 200)
frame.set_canvas_background('Teal')


# start frame
frame.start()
