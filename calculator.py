from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("380x400")
root.title("Python Calculator")
root.resizable(0, 0)

inp = StringVar()
myFont = font.Font(size=12)

screen = Entry(root, textvariable=inp, width=30, justify='right', font=(10), bd=4)
screen.grid(row=0, columnspan=4, padx=15, pady=15, ipady=5)

key_matrix = [["c", u"\u221A", "/", "<-"], 
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"], 
              ["1", "2", "3", "+"],
              ["!", "0", ".", "="]]

btns = []

def on_click(btn_text):
    if btn_text == "c":
        inp.set("")
    elif btn_text == "<-":
        inp.set(inp.get()[:-1])
    elif btn_text == "=":
        try:
            inp.set(eval(inp.get()))
        except:
            inp.set("Error")
    elif btn_text == u"\u221A":
        try:
            inp.set(float(inp.get()) ** 0.5)
        except:
            inp.set("Error")
    elif btn_text == "!":
        try:
            num = int(inp.get())
            fact = 1
            for i in range(1, num + 1):
                fact *= i
            inp.set(fact)
        except:
            inp.set("Error")
    else:
        inp.set(inp.get() + str(btn_text))

row_val = 1
for r in key_matrix:
    col_val = 0
    for c in r:
        btn = Button(root, text=str(c), width=8, height=2, font=myFont, command=lambda x=c: on_click(x))
        btn.grid(row=row_val, column=col_val, padx=5, pady=5)
        col_val += 1
    row_val += 1

root.mainloop()
   
