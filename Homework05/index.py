# implementation of card game - Memory

import simplegui
import random

choice1 = 0
choice2 = 0

# helper function to initialize globals
def new_game():
    global num_list, cards_is_opened, opened, turns
    
    opened = 0
    turns = 0
    
    num_list = [i for i in range(0,8)] + [i for i in range(0,8)]
    random.shuffle(num_list)
    print num_list
    
    cards_is_opened = [False] * 16
    label.set_text("Turns = 0")
    pass  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global choice1, choice2, cards_is_opened, opened, turns
    
    ev_click =  pos[0] // 50
    
    if opened == 0:
        opened = 1
        choice1 = ev_click
        cards_is_opened[choice1] = True
    elif opened == 1 and cards_is_opened[ev_click] != True:
        opened = 2
        choice2 = ev_click
        cards_is_opened[choice2] = True
        turns += 1
    elif opened == 2 and cards_is_opened[ev_click] != True:
        if num_list[choice1] == num_list[choice2]:
            pass
        else:
            cards_is_opened[choice1] = False
            cards_is_opened[choice2] = False
            
        opened = 1
        choice1 = ev_click
        cards_is_opened[choice1] = True

    label.set_text("Turns = " + str(turns))
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global num_list
    for i in range(0, 16):
        if cards_is_opened[i]:
            canvas.draw_text(str(num_list[i]), (50 * i + 10, 60), 40, 'white')
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * i, 100), (50 * i + 50, 100), (50 * i + 50, 0)], 3, 'red', 'green')
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric
