import tkinter as tk
from tkinter import messagebox
from random import randint
import time
root = tk.Tk()
  
WIDTH = 500
HEIGHT = 500
label = tk.Label(root, text="Use arrow keys to move", font = 'Bold')
label.pack()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
  
canvas.pack()
  
 
x1 = WIDTH / 2
y1 = HEIGHT / 2
  
 
 
player = canvas.create_oval(x1, y1, x1 + 40, y1 + 40, fill = 'green', width = '5', outline = 'Blue')
 
time_label = tk.Label(root,text = 'Time left (seconds): ', fg = 'Green', font = 'Bold')
time_label.pack()
 
score = 0
start_time = 0
duration = 10
opponents = randint(8,20)
 
score_string_var = tk.StringVar()
score_string_var.set('Score: {}'.format(score))
 
 
score_label = tk.Label(textvariable = score_string_var, font = 'Bold')
score_label.pack()
 
timer = None
def update_clock():
    now = time.time()
    global timer
    timer = root.after(1000, update_clock)
    seconds_diff = int(now) - int(start_time)
    time_label.configure(text = "Time left(seconds): {}".format(duration-seconds_diff))
    if seconds_diff > duration:
        for canvas_widget in canvas.find_all():
            if canvas_widget != player:
                canvas.delete(canvas_widget)
        root.after_cancel(timer)
        time_label.configure(text = 'Game over, time up!', fg = 'red', font = 'Bold')
        global score
        messagebox.showinfo(title=None, message="Well done, your score is: {} out of {}!".format(score, opponents))
 
 
 
 
def overlapping_helper():
    s = canvas.bbox(player)
    overlapping_result = canvas.find_overlapping(s[0], s[1], s[2], s[3])
 
     
    if len(overlapping_result) > 1:
        canvas.delete(overlapping_result[1])
        global score
        score += 1
        score_string_var.set("Score: {}".format(score))
 
 
def move(event):
    overlapping_helper()
     
    if event.keysym == "Left":
        current_coords = canvas.coords(player)
        if current_coords[0] <= 0:
            canvas.move(player, WIDTH, 0)
        else:
            canvas.move(player, -15, 0)
    elif event.keysym == "Right":
        current_coords = canvas.coords(player)
        if current_coords[0] >= WIDTH:
            canvas.move(player, -WIDTH, 0)
        else:
            canvas.move(player, 15, 0)
    elif event.keysym == "Up":
        current_coords = canvas.coords(player)
        if current_coords[1] <= 0:
            canvas.move(player, 0, HEIGHT)
        else:
            canvas.move(player, 0, -15)
         
    elif event.keysym == "Down":
        current_coords = canvas.coords(player)
        if current_coords[1] >= HEIGHT:
            canvas.move(player, 0, -HEIGHT)
        else:
            canvas.move(player, 0, 15)
 
def setup():
    for i in range(opponents):
        random_color = get_random_color()
        x = randint(10, WIDTH - 15)
        distance = randint(5,30)
        y = randint(10, HEIGHT - 15)
        canvas.create_oval(x, # x0
        y, # y0
        x+distance, # x1
        y+distance , # y1
        fill = random_color)
 
def get_random_color():
    r = lambda: randint(0,255)
    return '#%02X%02X%02X' % (r(),r(),r())
 
setup()
start_time = time.time()
update_clock()
root.bind("<KeyPress>", move)
root.mainloop()