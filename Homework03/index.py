# Testing template for format function in "Stopwatch - The game"

###################################################
# Student should add code for the format function here

import simplegui

#######

time = 0
interval = 100

stops_attempts = 0
successful_attempts = 0

stop = True
print "Running:" + str(not stop)

#######

def time_counter():
    global time
    
    time += 1
    
    if time == 6000:
        timer.stop()
        print "Sorry, you lose. (inaction)"
        reset_tip.set_text("Sorry, you lose. (inaction)")

    return str(time)
    
def draw(canvas):
    canvas.draw_text(format(time), [200,200], 36, "White")
    
    draw_attempts = '%d / %d' % (successful_attempts, stops_attempts)
    canvas.draw_text(str(draw_attempts), [215,40], 36, "Yellow")
    
def start_act():
    global stop
    
    timer.start()
    
    stop = False
    print "Running:" + str(not stop)
    return stop
    
def stop_act():
    global stop
    global stops_attempts
    global successful_attempts
    
    if stop == False:
        stops_attempts += 1
    
    if format(time)[-1] == '0' and stop == False:
        successful_attempts += 1
    
    
    timer.stop()
    reset_tip.set_text('')
    stop = True
    
    print "Running:" + str(not stop)
    return stop

def reset_act():
    global time
    global stop
    global stops_attempts
    global successful_attempts

    if stop == True:
        time = 0
        stops_attempts = 0
        successful_attempts = 0
    else:
        reset_tip.set_text('First you must stop the timer')

def format(t):
    lenth = len(str(t))
    zerr = 4 - lenth
    if zerr != 0:
        res = zerr * '0' + str(t)
    else:
        res = str(t)
    return str(int(res[:2])/6) + ":" + str(int(res[:2])%6) + res[-2] + "." + res[-1]

#######

frame = simplegui.create_frame("Stop: game", 500, 500)
frame.set_canvas_background("Blue")


timer = simplegui.create_timer(interval, time_counter)



frame.set_draw_handler(draw)

frame.add_button("Start", start_act, 200)
frame.add_button("Stop", stop_act, 200)
frame.add_button("Reset", reset_act, 200)

reset_tip = frame.add_label('', 500)

frame.start()

###################################################