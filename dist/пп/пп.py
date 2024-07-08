import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

Window1 = Tk()
Window1.withdraw()
Window = Tk()
Window.geometry("400x400")
Window.maxsize(400,400)
Window.minsize(400,400)
mas = ["1","2",'3','4','5','6','7','8','9','0']
famyenty =""
nameenty=""
Enter = True
x=0
def Zapla():
    global Goldi
    def zaplata():
        global Hour
        x1T = False
        x2T = False
        x1=0
        x2=0
        Day = DayEnty.get()
        Hour = entyHour.get()
        for i in range (len(Hour)):
            for j in range (len(mas)):
                if Hour[i]==mas[j]:
                    x1+=1
        if x1==len(Hour):
            x1T = True
        for i in range(len(Day)):
            for j in range(len(mas)):
                if Day[i] == mas[j]:
                    x2 += 1
        if x2 == len(Day):
            x2T = True
        if x1T and x2T:
            Hourint = int(Hour)
            if Hourint>24:
                Hourint=24
            elif Hourint<0:
                Hourint=0
            Dayint = int(Day)
            if Dayint>31:
                Dayint=31
            elif Dayint<0:
                Dayint=0
            zarplata = x*Dayint*Hourint
            lbl = ttk.Label(Window1, text=zarplata).pack()
        else:
            showerror(title="Ошибка входа", message="Неверный данные")
    def Hours():
        global entyHour
        lbl = ttk.Label(Window1, text = "Сколько часов в день работаете?").pack()
        entyHour = ttk.Entry(Window1)
        entyHour.pack()
        btn = ttk.Button(Window1, text = "Расчитать разплату", command = zaplata).pack()
    def HoursStol():
        global DayEnty
        lbl = ttk.Label(Window1, text="Скольчо дней было отработанно?").pack()
        DayEnty = ttk.Entry(Window1)
        DayEnty.pack()
        btn = ttk.Button(Window1, text = "Выбрать кол-во часов", command = Hours).pack()

    def gord():
        global x
        Goldi = combobox.get()
        Goldi = Goldi.rstrip('\n')
        if Goldi == "Cook/Chef":
            x=400
        if Goldi == "Manager":
            x=500
        if Goldi == "Bartender":
            x=300
        if Goldi == "Busser":
            x =350
        if Goldi == "Waiter/Waitress":
            x=300
        HoursStol()

    global Window1
    lbl = ttk.Label(Window1, text = "Выберите должность").pack()
    file = open("Должности.txt", "r")
    Dolg = file.readlines()
    combobox = (ttk.Combobox(Window1, values=Dolg))
    combobox.pack()
    btn = ttk.Button(Window1, text="Выбрать должность", command=gord).pack()
def Sosdanie():
    global Enter
    global Window1
    btnPR = True
    Enter = False
    Window1 = Tk()
    Window1.geometry("400x400")
    Window1.minsize(400,400)
    Window1.maxsize(400,400)
    Window.withdraw()
    Window1.protocol("WM_DELETE_WINDOW", lambda: Window.destroy())
    labl = ttk.Label(Window1, text = "Хотите расчитать зарплату?").pack()
    btn = ttk.Button(Window1, text = "Расчитать зарплату", command = Zapla).pack()
def enter():
    global Enter
    famyenty = famyEntry.get()
    nameenty = nameEntry.get()
    vseenty = famyenty+"="+nameenty
    with open("Логин.txt", "r") as file:
        for i, line in enumerate(file):
            line = line.rstrip('\n')
            if vseenty==line:
                Sosdanie()
    if Enter:
        showerror(title = "Ошибка входа", message = "Неверный логин или пароль")


def password():
    WindowPassword = Tk()
    WindowPassword.geometry("400x400")
    WindowPassword.maxsize(400,400)
    WindowPassword.minsize(400,400)
    label = ttk.Label(WindowPassword, text = "Обратитесь в службу поддержки. 8-800-555-35-35").pack()

LabelFIO = ttk.Label(Window, text = "Введите логин и пароль").pack()
famyEntry = ttk.Entry(Window)
famyEntry.pack()
nameEntry = ttk.Entry(Window)
nameEntry.pack()
btnFIO = ttk.Button(Window, text = "Войти", command = enter).pack()
ButtonPass = ttk.Button(Window, text = "Забыли пароль?", command = password).pack()


Window.mainloop()