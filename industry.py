from tkinter import * 
import tkinter


#工业
class Industry:
    Nalgfar = 'nalgfar'

#材料
class Material:
    def __init__(self,Tritanium,Pyerite, Mexallon, Isogen, Nocxium, Zydrine, Megacyte):
        self.Tritanium = Tritanium
        self.Pyerite = Pyerite
        self.Mexallon = Mexallon
        self.Isogen = Isogen
        self.Nocxium = Nocxium
        self.Zydrine = Zydrine
        self.Megacyte = Megacyte

#船只种类
class Nalgfar:
    material = Material

#蓝图
class Blueprint:
    Capital_Propulsion_Engine = Material(457050,110416,41994,6938,2110,604,302)
    Capital_Turret_Hardpoint = Material(546912,113826,45010,7760,2358,876,386)
    Capital_Sensor_Cluster = Material(443591,101026,40877,6659,1804,666,298)
    Capital_Armor_Plates = Material(473141,111118,43324,7109,2141,682,304)
    Capital_Capacitor_Battery = Material(326873,107842,39547,6440,1841,660,280)
    Capital_Power_Generator = Material(510149,110413,45621,7491,2191,729,334)
    Capital_Shield_Emitter = Material(498880,104957,43194,7269,2033,696,332)
    Capital_Jump_Drive = Material(749916,142710,49913,8617,2249,908,444)
    Capital_Computer_System = Material(427708,111110,44110,6581,1858,648,296)
    Capital_Construction_Parts = Material(388208,93777,37729,5104,1530,538,212)
    Capital_Siege_Array = Material(555658,125277,47249,7916,2438,908,428)
    Capital_Ship_Maintenance_Bay = Material(576759,189942,53312,9010,246,1914,416)
    Capital_Corporate_Hanger_Bay = Material(583442,145664,51297,9321,2678,938,436)

#材料成本
def MaterialCost(name):
    return
    #win_cost

#战舰选择
def Ship_Choice():
    ship_win=tkinter.Tk()
    ship_win.title("战舰选择")
    ship_win.geometry('800x500')
    button_nalgfar=tkinter.Button(ship_win,text='Nalgfar',command=lambda:Ship_Panel('Nalgfar'))
    button_nalgfar.pack()
    button_nalgfar.place(x=10,y=10)
    ship_win.mainloop()
    return

#战舰详细信息
def Ship_Panel(name):
    panel=tkinter.Tk()
    panel.title(name)
    panel.geometry('500x500')
    panel.mainloop()
    return

win=tkinter.Tk()
win.title("工业")
win.geometry('1000x500')
button1=tkinter.Button(win,text='成本',command=Ship_Choice) 
button1.pack()
button1.place(x=10,y=10)
win.mainloop()