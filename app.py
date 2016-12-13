"""
    --Authors--
    Morgan Mitchell
    Andrew Goodman

    --Date--
    December 12, 2016

    Recur application prototype
"""
from tkinter import *
from modules.system.SystemData import SystemData
from modules.database.DbInteract import dbtest

# Initialize app
root = Tk()
root.title("Recur Prototype v0.01")
#root.resizable(width=False,height=False)

# Create top frame
topFrame = Frame(root,width=300,height=400)
topFrame.grid(column=0,row=0,columnspan=3,rowspan=2,sticky=(N,E,S,W))

# Create bottom frame
bottomFrame = Frame(root)
bottomFrame.grid(column=0,row=3,columnspan=3,rowspan=2,sticky=(S))

scroll = Scrollbar(topFrame)

txt = Text(topFrame,width=50,height=50)
txt.grid(column=1,row=1,columnspan=2,rowspan=2,sticky=(N))

scroll.config(command=txt.yview)
txt.config(yscrollcommand=scroll.set)

btn = Button(bottomFrame,text="Query Test")
query_text = dbtest(None)
btn.bind('<Button-1>',dbtest)
btn.grid(column=1,row=3,columnspan=2,rowspan=1,sticky=(S))

txt.insert("end",query_text)

root.mainloop()
