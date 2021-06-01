from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
import pyodbc

conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=I:\Git\python_note\note-python/bd_4.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
crsr.execute('select * from lab_1')

def daf():
    #for string in crsr.fetchall():
    #    return(string)
    row = crsr.fetchone()
    return(row)

def sel(num):
    crsr_1 = cnxn.cursor()
    crsr_1.execute('select Key from lab_1 where key = '+num+'')
    res = crsr_1.fetchone()
    num_str.configure(text = res)

window = Tk()
window.title("Data Base lab 10")

num_str = Label(window, text="Key")  
num_str.grid(column=0, row=0) 
key = Entry(window, width = 10, state = 'disabled')
key.grid(column = 1, row = 0)

Fio = Label(window, text="Full Name")  
Fio.grid(column=0, row=1) 
full_name = Entry(window, width = 10, state = 'disabled')
full_name.grid(column = 1, row = 1)

num_bil = Label(window, text="Number of stud ID")  
num_bil.grid(column=0, row=2)
id = Entry(window, width = 10, state = 'disabled')
id.grid(column = 1, row = 2) 

num_zac = Label(window, text="Number of score book")  
num_zac.grid(column=2, row=0)
s_book = Entry(window, width = 10, state = 'disabled')
s_book.grid(column = 3, row = 0)

group = Label(window, text="Number of group")  
group.grid(column=2, row=1)
grp = Entry(window, width = 10, state = 'disabled')
grp.grid(column = 3, row = 1)

b_day = Label(window, text="Date of Birthday")  
b_day.grid(column=2, row=2)
bday = Entry(window, width = 10, state = 'disabled')
bday.grid(column = 3, row = 2)

place_b = Label(window, text="Bday place")  
place_b.grid(column=4, row=0)
place = Entry(window, width = 10, state = 'disabled')
place.grid(column = 5, row = 0)

home = Label(window, text="Home addres")  
home.grid(column=4, row=1)
hm = Entry(window, width = 10, state = 'disabled')
hm.grid(column = 5, row = 1)

phone = Label(window, text="Phone number")  
phone.grid(column=4, row=2)
phn = Entry(window, width = 10, state = 'disabled')
phn.grid(column = 5, row = 2)

delet = Button(window, text="Delete")  
delet.grid(column=5, row=4)

add = Button(window, text = "Add")
add.grid(column = 2, row = 3)

dell = Button(window, text = "Delete")
dell.grid(column = 3, row = 3)

chg = Button(window, text = "Change")
chg.grid(column = 4, row = 3)

stud = Label(window, text="Does it need a hostel?")  
stud.grid(column=0, row=3)
combo = Combobox(window)  
combo['values'] = ('Yes', 'No')  
combo.grid(column=1, row=3) 

cmb = Combobox(window)  
cmb['values'] = ('1', '2', '3', '4', '5')
cmb.current(0)  
cmb.grid(column=5, row=3)

df = daf()
txt1 = scrolledtext.ScrolledText(window, width=40, height=5)  
txt1.grid(column=0, row=4)  
txt1.insert(INSERT, df)

df = daf()
txt2 = scrolledtext.ScrolledText(window, width=40, height=5)  
txt2.grid(column=1, row=4)  
txt2.insert(INSERT, df)

df = daf()
txt3 = scrolledtext.ScrolledText(window, width=40, height=5)  
txt3.grid(column=2, row=4)  
txt3.insert(INSERT, df)

df = daf()
txt4 = scrolledtext.ScrolledText(window, width=40, height=5)  
txt4.grid(column=3, row=4)  
txt4.insert(INSERT, df)

df = daf()
txt5 = scrolledtext.ScrolledText(window, width=40, height=5)  
txt5.grid(column=4, row=4)  
txt5.insert(INSERT, df)

upd = Button(window, text="Update", command = sel(cmb.get()))  
upd.grid(column=5, row=5)

window.mainloop()