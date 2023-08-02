import tkinter
from tkinter import *
from tkinter import ttk
from pwpullergit import pwOutput
import os

main = Tk()
main.geometry("220x300")
main.title("bws pws")
main.iconbitmap("benguin.ico")
lbframe = Frame(main)
lbscroll = ttk.Scrollbar(lbframe, orient=VERTICAL)
lbscroll.config(command=Listbox.yview)
lbscroll.pack(side=RIGHT, fill=Y)
lbframe.pack()

listbox = tkinter.Listbox(lbframe, width=35, height=15 , bd=1, bg="#F5F5F6",
                          selectbackground="#6600C1" ,relief=RIDGE, yscrollcommand=lbscroll.set)
listbox.pack()



def myClick():
    pw = pwOutput()
    listbox.insert(END,str(pw))

def clear():
    main.destroy()
    os.startfile("bwpw.exe")

myButton = ttk.Button(main, text="pw generator :D", width=30, command=myClick)
myButton.pack()

clearbtn=ttk.Button(main,text='restart',command=clear)
clearbtn.pack()

main.mainloop()
