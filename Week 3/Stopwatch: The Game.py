# coding=utf-8
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

__author__ = 'João Silva'

# define global variables
timer_counter = 0
successful_stops_counter = 0
total_stops_counter = 0
second = 10
ten_seconds = second * 10
minute = second * 60


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format_time(t):
    a = t / minute
    b = (t / ten_seconds) % 6
    c = (t / second) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    if not timer.is_running():
        timer.start()


def stop_handler():
    global total_stops_counter, successful_stops_counter
    if timer.is_running():
        timer.stop()
        total_stops_counter += 1
        if (timer_counter % 10) == 0:
            successful_stops_counter += 1


def reset_handler():
    global timer_counter, successful_stops_counter, total_stops_counter
    stop_handler()
    timer_counter = 0
    successful_stops_counter = 0
    total_stops_counter = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global timer_counter
    timer_counter += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format_time(timer_counter), (70, 80), 30, 'White')
    canvas.draw_text(str(successful_stops_counter) + "/" + str(total_stops_counter),
                     (150, 30), 30, 'Green')


# create frame
frame = simplegui.create_frame('Testing', 200, 150)
button_start = frame.add_button('Start', start_handler, 200)
button_stop = frame.add_button('Stop', stop_handler, 200)
button_reset = frame.add_button('Reset', reset_handler, 200)

# create timer
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()
