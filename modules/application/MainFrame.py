"""
    Andrew Goodman
    December 14, 2016

    The main UI window
"""
from tkinter import *
from modules.database.DbInteract import *


class MainFrame():
    """The main frame of the application"""

    def __init__(self,master,ver):
        """Initializes the MainFrame class"""

        master.title("Recur App Prototype")

        frame = Frame(master)
        frame.grid(column = 0,row = 0,sticky = (N,E,S,W))

        # Reads the current version number of the application
        versionNumber = ver

        welcomeLabel = Label(frame,text = "Welcome to the Recur App Prototype\n \
            Current Version {0}".format(versionNumber))
        welcomeLabel.grid(column = 0,row = 0,sticky = (N,E,S,W))

        # Memeber variables
        self.query = StringVar()

        # Text area
        self.scroll = Scrollbar(frame)

        self.txt = Text(frame,width = 50,height = 10)
        self.txt.grid(column = 0,row = 1,rowspan = 2,sticky = (N,E,S,W))

        self.scroll.config(command = self.txt.yview)
        self.txt.config(yscrollcommand = self.scroll.set)

        # Query entry field
        self.queryEntry = Entry(frame,width=50,textvariable=self.query)
        self.queryEntry.grid(column = 0,row = 2,rowspan = 2,sticky = (N,E,S,W))

        # Query execute Button
        self.queryExecute = Button(frame,text="Query Test", \
            command=lambda:dbtest('<Button-1>',self.query.get(),self.txt))
        self.queryExecute.grid(column = 0,row = 4,sticky = (N,E,S,W))

        # Quit button that will exit the application
        self.exit = Button(frame,text = "Quit",command = frame.quit)
        self.exit.grid(column = 0,row = 5,sticky = (N,E,S,W))
