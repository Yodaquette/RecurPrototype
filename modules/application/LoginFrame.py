"""
    Andrew Goodman
    December 15, 2016

    The screen where registered users will log in
"""
import tkinter as tk
from tkinter import ttk
from modules.database.DbInteract import login
from modules.application.Registration import Registration


class LoginFrame(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lblWelcome = tk.Label(self,text = "Please log in")
        lblWelcome.grid(column = 0,row = 0,columnspan = 2,sticky = "nsew")
        #lblWelcome.pack(side = "left",fill = "both")

        # Variables to store username and password
        username = tk.StringVar()
        password = tk.StringVar()

        # Labels for username and password
        lblUsername = tk.Label(self,text = "Username:")
        lblPassword = tk.Label(self,text = "Password:")
        lblUsername.grid(column = 0,row = 1,sticky = "e")
        lblPassword.grid(column = 0,row = 2,sticky = "e")

        # Text entry forms for username and password
        entryUsername = tk.Entry(self,width = 25,textvariable = username)
        entryPassword = tk.Entry(self,width = 25,textvariable = password)
        entryUsername.grid(column = 1,row = 1,sticky = "W")
        entryPassword.grid(column = 1,row = 2,sticky = "W")

        # Login button
        btnLogin = ttk.Button(self,text = "Login", \
            command = lambda:login('<Button-1>',parent,username.get(),password.get()))
        btnLogin.grid(column = 0,row = 3,sticky = "sew")

        # Register button
        btnRegister = ttk.Button(self,text = "Register", \
            command = lambda:parent.display(Registration))
        btnRegister.grid(column = 1,row = 3,sticky = "sew")
