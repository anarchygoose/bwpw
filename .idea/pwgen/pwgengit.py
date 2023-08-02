import tkinter
from tkinter import *
from tkinter import ttk
from pwgenerator import pwOutput
import os

main = Tk()
main.geometry("220x300")
main.title("bws pws")
main.iconbitmap("benguin.ico")

#attempting to make scrollbar \/
main_frame = Frame(main)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame, borderwidth=0)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#not working scrollbar
#my_scrollbar = ttk.Scrollbar(my_canvas, orient=VERTICAL, command=my_canvas.yview)
#my_scrollbar.pack(side=RIGHT, fill=Y)

#my_canvas.configure(yscrollcommand=my_scrollbar.set)
#my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")
my_canvas.configure(scrollregion=my_canvas.bbox("all"))


#pw generator
def myClick():
    pw = pwOutput()
    label1 = tkinter.Entry(my_canvas,bd=0, textvariable=pw)
    label1.insert(0,str(pw))
    label1.config(state = "readonly")
    label1.pack()
    return label1

def clear():
    main.destroy()
    os.startfile("bwpw.exe")

clearbtn=ttk.Button(main,text='restart',command=clear)
clearbtn.pack()

myButton = ttk.Button(my_canvas, text="pw generator :D", width=20, command=myClick)
myButton.pack()
main.mainloop()
