"""
    Andrew Goodman
    December 14, 2016

    The main UI window
"""
import tkinter as tk
from modules.database.DbInteract import *

versionNumber = "v0.01"


class MainFrame(tk.Frame):
    """The main frame of the application"""

    def __init__(self,parent,controller):
        """Initializes the MainFrame class"""

        tk.Frame.__init__(self,parent)

        welcomeLabel = Label(self,text = "Welcome to the Recur App Prototype\n \
            Current Version {0}".format(versionNumber))
        welcomeLabel.grid(column = 0,row = 0,sticky = "nsew")

        # Memeber variables
        self.query = StringVar()

        # Text area
        self.scroll = Scrollbar(self)

        self.txt = Text(self,width = 50,height = 10)
        self.txt.grid(column = 0,row = 1,rowspan = 2,sticky = "nsew")

        self.scroll.config(command = self.txt.yview)
        self.txt.config(yscrollcommand = self.scroll.set)

        # Query entry field
        self.queryEntry = Entry(self,width=50,textvariable=self.query)
        self.queryEntry.grid(column = 0,row = 2,rowspan = 2,sticky = "nsew")

        # Query execute Button
        self.queryExecute = Button(self,text="Query Test", \
            command=lambda:dbtest('<Button-1>',self.query.get(),self.txt))
        self.queryExecute.grid(column = 0,row = 4,sticky = "nsew")

        # Quit button will exit the application
        self.exit = Button(self,text = "Quit",command = self.quit)
        self.exit.grid(column = 0,row = 5,sticky = "nsew")
