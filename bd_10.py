from tkinter import *
from tkinter.ttk import Combobox 

window = Tk()
window.title("Data Base lab 10")

num_str = Label(window, text="Key")  
num_str.grid(column=0, row=0) 

Fio = Label(window, text="Full Name")  
Fio.grid(column=0, row=1) 

num_bil = Label(window, text="Number of stud ID")  
num_bil.grid(column=0, row=2) 

num_zac = Label(window, text="Number of score book")  
num_zac.grid(column=2, row=0)

group = Label(window, text="Number of group")  
group.grid(column=2, row=1)

b_day = Label(window, text="Date of Birthday")  
b_day.grid(column=2, row=2)

place_b = Label(window, text="Bday place")  
place_b.grid(column=4, row=0)

home = Label(window, text="Home addres")  
home.grid(column=4, row=1)

phone = Label(window, text="Phone number")  
phone.grid(column=4, row=2)

stud = Label(window, text="Does it need a hostel?")  
stud.grid(column=0, row=3)

combo = Combobox(window)  
combo['values'] = ('Yes', 'No')  
combo.grid(column=1, row=3) 

window.mainloop()