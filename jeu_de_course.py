from tkinter import*
from turtle import*

def circuit_droit():
    global  x1 , x2 
    can1.create_line( x1 , 500 , x2 , 5 )

def modifier():
    global x1 , x2
    x1 = x1 + 300
    x2 = x2 + 300
    circuit_droit()


def colorier():
    goto(235,224)
    fill("black")

x1 = 100
x2 = 100
   
fen1 = Tk()

can1 = Canvas(fen1,bg="white",height=500,width=500)
can1.pack()

bou = Button(fen1,text="1",command = 
circuit_droit()

modifier()

colorier()

fen1.mainloop()


