"""
    --Authors--
    Morgan Mitchell
    Andrew Goodman

    --Date--
    December 12, 2016

    Recur application prototype
"""
from tkinter import *
from modules.application.MainFrame import MainFrame
from modules.system.SystemData import SystemData

versionNumber = "v0.01"

# Initialize app
root = Tk()
mainFrame = MainFrame(root,versionNumber)
#root.title("Recur Prototype v0.01")
#root.resizable(width=False,height=False)

# # Create top frame
# topFrame = Frame(root,width=300,height=400)
# topFrame.grid(column=0,row=0,columnspan=3,rowspan=2,sticky=(N,E,S,W))
#
# # Create bottom frame
# bottomFrame = Frame(root)
# bottomFrame.grid(column=0,row=3,columnspan=3,rowspan=2,sticky=(S))
#
# # Will store a query entered by the user
# query = StringVar()
#
# queryEntry = Entry(bottomFrame,width=100,textvariable=query)
# queryEntry.grid(column=2,row=3,sticky=(W,E))
#
# scroll = Scrollbar(topFrame)
#
# txt = Text(topFrame,width=50,height=10)
# txt.grid(column=0,row=0,columnspan=2,rowspan=2,sticky=(N))
#
# scroll.config(command=txt.yview)
# txt.config(yscrollcommand=scroll.set)
#
# btn = Button(bottomFrame,text="Query Test",command=lambda:dbtest('<Button-1>',query.get()))
# #_dbtest = partial(dbtest,query.get())
# #btn.bind('<Button-1>',lambda:dbtest('<Button-1>',query.get()))
# btn.grid(column=1,row=4,columnspan=2,rowspan=1,sticky=(S))



root.mainloop()
