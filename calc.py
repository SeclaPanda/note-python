from tkinter import *
from tkinter import scrolledtext
window = Tk()
window.title("Secla's Calc")

def pl(number):
    an = int(number) + int(number)
    num_str.configure(state = 'normal')
    num_str.insert(END, an)
    num_str.yview(END)
    num_str.configure(state = "disabled")
    

def mi():
    return mi - mi

def mul():
    return mul * mul

def de():
    return de / de

def answ(answer):
    num_str.configure(state = 'normal')
    num_str.insert(END, pl(answer))
    num_str.yview(END)
    num_str.configure(state = "disabled")

number = int()
answer = int()

num_str = scrolledtext.ScrolledText(window, width=25, height=1, state = "disabled")  
num_str.grid(column=1, row=0) 

disp = Entry(window, width=25, textvariable= number)
disp.grid(column= 0, row= 0)
disp.focus()

plus = Button(window, text= "+")
plus.grid(column= 0, row= 1)
plus.bind("<Button-1>", pl(number))

minus = Button(window, text= "-")
minus.grid(column= 1, row= 1)

mult = Button(window, text= "*")
mult.grid(column= 2, row= 1)

dec = Button(window, text= "/")
dec.grid(column= 3, row= 1)

equ = Button(window, text= "=")
equ.grid(column= 4, row= 1)
equ.bind("<Button-1>", answ(pl(number)))



window.mainloop()