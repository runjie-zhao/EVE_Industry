from tkinter import * 
import tkinter

#工业
class Industry:
    Nalgfar = 'nalgfar'

#材料成本
def MaterialCost():
    return
    #win_cost

def Ship_Choice():
    ship_win=tkinter.Tk()
    ship_win.title("战舰选择")
    ship_win.geometry('800x500')
    win.mainloop()


win=tkinter.Tk()
win.title("工业")
win.geometry('1000x500')
button1=Button(win,text='成本',command=Ship_Choice) 

button1.pack()
button1.place(x=10,y=10)
win.mainloop()