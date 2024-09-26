import tkinter as tk

root=tk.Tk()
WIDTH = 600
HEIGHT = 600

canvas=tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.pack()

x1 = WIDTH/2
y1 = HEIGHT/2

square = canvas.create_rectangle(x1-15, y1-15, x1+15,x1+15,outline="black",fill="red")
square2 = canvas.create_rectangle(x1-15, y1-15, x1+15,x1+15,outline="black",fill="yellow")
square3 = canvas.create_rectangle(x1-15, y1-15, x1+15,x1+15,outline="black",fill="green")
square4 = canvas.create_rectangle(x1-15, y1-15, x1+15,x1+15,outline="black",fill="blue")

 
def redraw():
   canvas.after(15,redraw)
   canvas.move(square,-2,2)
   canvas.move(square2,2,2)
   canvas.move(square3,-2,-2)
   canvas.move(square4,2,-2)

redraw()
   
root.mainloop()