"""
    Andrew Goodman
    December 15, 2016

    Controls the application
"""
import tkinter as tk
from modules.application.LoginFrame import LoginFrame
from modules.application.Registration import Registration
from modules.application.MainFrame import MainFrame


class ApplicationController(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        # Use custom app icon
        #tk.Tk.iconbitmap(self,default = "AppIcon.ico")

        app = tk.Frame(self)
        app.grid(column = 0,row = 0,sticky = "nsew")
        #app.pack(side = "top",fill = "both",expand = True)

        app.grid_rowconfigure(0,weight = 1)
        app.grid_columnconfigure(0,weight = 1)

        # Declare empty dictionary to store app frames
        self.appFrames = {}

        for frame in (LoginFrame,Registration,MainFrame):
            appFrame = frame(self,app)
            self.appFrames[frame] = appFrame
            appFrame.grid(column = 0,row = 0,sticky = "nsew")

        # Set start frame
        self.display(LoginFrame)

    def display(self,frame):
        """Display a frame"""
        currentFrame = self.appFrames[frame]
        currentFrame.tkraise()
