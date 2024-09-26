from tkinter import *
import tkinter.messagebox as messagebox
import globals as gl

def check_login():
    txtUsername = gl.GlobalComponents.get("txtUsername")
    txtPassword = gl.GlobalComponents.get("txtPassword")
    if txtUsername.get() == "admin" and txtPassword.get() == "1234":
        messagebox.showinfo("Success", "You have successfully logged in.")
    else:
        messagebox.showerror("Error", "Invalid credentials!") 

window = Tk()
window.title("Login form")
window.geometry("350x250")
DEFAULT_FONT = ("Arial", 20)

# btn - Button lbl - Label, txt - Entry
lblUsername = Label(window, font=DEFAULT_FONT, text="Username")
lblPassword = Label(window, font=DEFAULT_FONT, text="Password")
txtUsername = Entry(window, font=DEFAULT_FONT)
txtPassword = Entry(window, font=DEFAULT_FONT, show="*")
btnLogin = Button(window, font=DEFAULT_FONT, text="Login",
                  command=check_login)
gl.GlobalComponents.set("txtUsername", txtUsername)
gl.GlobalComponents.set("txtPassword", txtPassword)

lblUsername.place(x=10, y=10)
txtUsername.place(x=10, y=50)
lblPassword.place(x=10, y=80)
txtPassword.place(x=10, y=120)
btnLogin.place(x=105,y=170)


if __name__ == "__main__":
    window.mainloop()