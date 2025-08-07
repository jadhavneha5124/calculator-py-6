#Assignment No 6
from tkinter import *
window=Tk()
window.title("Neha's Calculator")
window.geometry("500x00")
entry=Entry(window , width = 50 , borderwidth = 5 )
entry.place(x = 0, y = 0)

def click(num):
    result=entry.get()
    entry.delete(0,END)
    entry.insert(0,str(result)+str(num))

b=Button(window,text="1",width=12,command=lambda: click(1))
b.place(x=10,y=60)

b=Button(window,text="2",width=12,command=lambda: click(2))
b.place(x=80,y=60)

b=Button(window,text="3",width=12,command=lambda: click(3))
b.place(x=170,y=60)

b=Button(window,text="4",width=12,command=lambda: click(4))
b.place(x=10,y=120)

b=Button(window,text="5",width=12,command=lambda: click(5))
b.place(x=80,y=120)

b=Button(window,text="6",width=12,command=lambda: click(6))
b.place(x=170,y=120)

b=Button(window,text="7",width=12,command=lambda: click(7))
b.place(x=10,y=180)

b=Button(window,text="8",width=12,command=lambda: click(8))
b.place(x=80,y=180)

b=Button(window,text="9",width=12,command=lambda: click(9))
b.place(x=170,y=180)

b=Button(window,text="0",width=12,command=lambda: click(0))
b.place(x=10,y=240)

def add():
    n1=entry.get()
    global math
    math="addition"
    global i
    i = int(n1)
    entry.delete(0,END)

b=Button(window,text="+",width=12,command=add)
b.place(x=80,y=240)

def sub():
    n1 = entry.get()
    global math
    math="subtraction"
    global i
    i = int(n1)
    entry.delete(0,END)

b=Button(window,text="-",width=12,command=sub)
b.place(x=170,y=240)

def mult():
    n1 = entry.get()
    global math
    math="multipiction"
    global i
    i = int(n1)
    entry.delete(0,END)

b=Button(window,text="*",width=12,command= mult)
b.place(x=10,y=300)

def div():
    n1 = entry.get()
    global math
    math = "division"
    global i
    i=int(n1)
    entry.delete(0,END)

b=Button(window,text="/",width=12,command= div)
b.place(x=80,y=300)

def equal():
    n2=entry.get()
    entry.delete(0,END)

    if math == "addition":
        entry.insert(0, i + int(n2))
    elif math == "subtraction":
        entry.insert(0, i - int(n2))
    elif math == "multiplication":
        entry.insert(0, i * int(n2))
    elif math == "division":
        entry.insert(0 , i / int(n2))

b=Button(window,text="=",width=12,command=equal)
b.place(x=170,y=300)

def clear():
    entry.delete(0,END)
b=Button(window,text="clear",width=12,command=clear)
b.place(x=10,y=360)
mainloop()











