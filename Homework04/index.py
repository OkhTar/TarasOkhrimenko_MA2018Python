# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [3*(-40.0 / 60.0),  3*(5.0 / 60.0)]

paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT

paddle1_vel = 0.0
paddle2_vel = 0.0

score1 = 0
score2 = 0

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [3*(-40.0 / 60.0),  3*(5.0 / 60.0)]
    
    speed_hor = random.randrange(1,3)
    #print speed_hor
    speed_vert = random.randrange(1,4)
    #print speed_vert
    
    if direction == 'RIGHT':
        print 'R'
        ball_vel[0] += 3* speed_hor
        ball_vel[1] += 3* -speed_vert
        print ball_vel
    elif direction == 'LEFT':
        print 'L'
        ball_vel[0] += -speed_hor
        ball_vel[1] += speed_vert
        print ball_vel
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    
    rand_start = random.randrange(0,2)
    print rand_start
    if rand_start == 1:
        spawn_ball('RIGHT') 
    else:
        spawn_ball('LEFT')
    
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT
    
    paddle1_vel = 0             
    paddle2_vel = 0 
    
    score1 = 0
    score2 = 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] -= ball_vel[1]
    
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] =- ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] =- ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT]], PAD_WIDTH, "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide    
    if ball_pos[0] <= 2*PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] < paddle1_pos or ball_pos[1] >= paddle1_pos + PAD_HEIGHT:
            spawn_ball('RIGHT')
            score2 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    elif ball_pos[0] >= WIDTH - 2*PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] < paddle2_pos or ball_pos[1] >= paddle2_pos + PAD_HEIGHT:
            spawn_ball('LEFT')
            score1 += 1
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
        
    # draw scores
    canvas.draw_text(str(score1), (170, 50), 36, "Red")
    canvas.draw_text(str(score2), (400, 50), 36, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    
    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel += 1
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel -= 1
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel += 1
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel -= 1
        
def keyup(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["down"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle2_vel = 0

def exit():
    frame.stop()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("New", new_game, 100)
frame.add_button("Exit", exit, 100)

# start frame
#new_game()
frame.start()

