from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.geometry("500x500")
mainframe = Frame(root)


def changeText():
    if myTextVar.get() == "This is text":
        myTextVar.set("This is different text")
    else:
        myTextVar.set("This is text")
    showinfo("show info", "This is info")
    showwarning("show warning", "this is a warning")
    result = askquestion("ask question", "this is a question")
    if result == "yes":
        print("yes")
    else:
        print("no")
def draw(event):
    x=event.x
    y=event.y
    cv.create_rectangle(x+5, y+5, x-5, y-5, fill="#123456", outline = "#123456")
def draw2(event):
    x=event.x
    y=event.y
    cv.create_oval(x+5, y+5, x-5, y-5, fill="#123456", outline = "#123456")
def draw3(event):
    x=event.x
    y=event.y
    cv.create_line(x+5, y+5, x-5, y-5, fill="#123456")
#widgets
myTextVar = StringVar()
myTextVar.set("This is text")
myLabel = Label(mainframe, textvariable = myTextVar)

myButton = Button(mainframe, text = "Change text", command = changeText)

myList = ["One", "Two", "Three", "Four", "Five"]
myListVar = StringVar()
myListVar.set("One")

mySpinbox = Spinbox(mainframe, textvariable = myListVar, values = myList)
myOptionMenu = OptionMenu(mainframe, myListVar, *myList)




cv = Canvas(mainframe, width = 300, height = 300, bg="#999999")
cv.bind("<Button-1>", draw)
cv.bind("<Button-2>", draw2)
cv.bind("<Button-3>", draw3)
#grid
mainframe.grid()
myLabel.grid(row=1,column=1)
myButton.grid(row=2, column=1, ipadx=5, ipady=10)

mySpinbox.grid(row=1, column=2)
myOptionMenu.grid(row=2, column=2)

cv.grid(row=3, column=1)
