from tkinter import *
import tkinter.messagebox as messagebox
import globals as gl

def addition_event():
    txtX = gl.GlobalComponents.get("txtX")
    txtY = gl.GlobalComponents.get("txtY")
    x = float(txtX.get())
    y = float(txtY.get())
    result = x + y 
    messagebox.showinfo("Rezultat", f"{x} + {y} = {result}")


def subtraction_event():
    txtX = gl.GlobalComponents.get("txtX")
    txtY = gl.GlobalComponents.get("txtY")
    x = float(txtX.get())
    y = float(txtY.get())
    result = x - y 
    messagebox.showinfo("Rezultat", f"{x} - {y} = {result}")

def multiplication_event():
    txtX = gl.GlobalComponents.get("txtX")
    txtY = gl.GlobalComponents.get("txtY")
    x = float(txtX.get())
    y = float(txtY.get())
    result = x * y 
    messagebox.showinfo("Rezultat", f"{x} * {y} = {result}")

def division_event():
    txtX = gl.GlobalComponents.get("txtX")
    txtY = gl.GlobalComponents.get("txtY")
    x = float(txtX.get())
    y = float(txtY.get())
    if y == 0:
        messagebox.showerror("Error", "Division by 0 is not allowed!")
    else:
        result = x / y 
        messagebox.showinfo("Rezultat", f"{x} / {y} = {result}")



window = Tk()
window.title("Calculator")
window.geometry("350x250")
DEFAULT_FONT = ("Arial", 20)

lblX = Label(window, text="X:", font=DEFAULT_FONT, width=4)
lblY = Label(window, text="Y:", font=DEFAULT_FONT, width=4)
txtX = Entry(window, font=DEFAULT_FONT, width=10)
txtY = Entry(window, font=DEFAULT_FONT, width=10)
btnAdd = Button(window, font=DEFAULT_FONT, text="+", width=4,
                command=addition_event)
btnSub = Button(window, font=DEFAULT_FONT, text="-", width=4,
                command=subtraction_event)
btnMul = Button(window, font=DEFAULT_FONT, text="*", width=4,
                command=multiplication_event)
btnDiv = Button(window, font=DEFAULT_FONT, text="/", width=4,
                command=division_event)
gl.GlobalComponents.set("txtX", txtX)
gl.GlobalComponents.set("txtY", txtY)

lblX.place(x=10, y=10)
txtX.place(x=90, y=10)
lblY.place(x=10, y=50)
txtY.place(x=90, y=50)
btnAdd.place(x=10, y=100)
btnSub.place(x=90, y=100)
btnMul.place(x=180, y=100)
btnDiv.place(x=270, y=100)

if __name__ == "__main__":
    window.mainloop()