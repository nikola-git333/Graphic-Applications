from tkinter import * 
import globals as gl

def convert_event():
    rbValue = gl.GlobalValues.get("rbValue")
    txtC = gl.GlobalComponents.get("txtC")
    lblConvert = gl.GlobalComponents.get("lblConvert")
    if rbValue.get() == "F":
        t = float(txtC.get()) * 1.8 + 32
        lblConvert["text"] = f"{txtC.get()}°C = {t}°F"
    else:
        t = float(txtC.get()) + 273.15
        lblConvert["text"] = f"{txtC.get()}°C = {t}K"
        

window = Tk()
window.title("Choices")
window.geometry("350x250")
DEFAULT_FONT = ("Arial", 20)

rbValue = StringVar(value="F")
gl.GlobalValues.set("rbValue", rbValue)
txtC = Entry(window, font=DEFAULT_FONT, width=10)
lblC = Label(window, font=DEFAULT_FONT, text="°C")
rbOption1 = Radiobutton(window, text="°F", value="F",
                        variable=rbValue, font=DEFAULT_FONT)
rbOption2 = Radiobutton(window, text="K", value="K",
                        variable=rbValue, font=DEFAULT_FONT)
lblConvert = Label(window, font=DEFAULT_FONT, text="")
btnConvert = Button(window, font=DEFAULT_FONT, text="Convert",
                    command=convert_event)
gl.GlobalComponents.set("txtC", txtC)
gl.GlobalComponents.set("lblConvert", lblConvert)
txtC.place(x=10,y=10)
lblC.place(x=165,y=10)
rbOption1.place(x=10, y=50)
rbOption2.place(x=90, y=50)
btnConvert.place(x=10, y=90)
lblConvert.place(x=10,y=145)


if __name__ == "__main__":
    window.mainloop()