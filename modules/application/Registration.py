"""
    Andrew Goodman
    December 19, 2016

    Regristration frame
"""
import tkinter as tk
from tkinter import ttk
from modules.database.DbInteract import register


class Registration(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        lblInstruction = tk.Label(self,text = "Please enter a username and password to register")
        lblInstruction.grid(column = 0,row = 0,columnspan = 2,sticky = "nsew")

        username = tk.StringVar()
        password = tk.StringVar()
        firstName = tk.StringVar()
        lastName = tk.StringVar()
        email = tk.StringVar()
        phone = tk.StringVar()

        lblUsername = tk.Label(self,text = "Username:")
        lblUsername.grid(column = 0,row = 1,sticky = "e")
        entryUsername = tk.Entry(self,width = 20,textvariable = username)
        entryUsername.grid(column = 1,row = 1,sticky = "w")

        lblPassword = tk.Label(self,text = "Password:")
        lblPassword.grid(column = 0,row = 2,sticky = "e")
        entryPassword = tk.Entry(self,width = 20,textvariable = password)
        entryPassword.grid(column = 1,row = 2,sticky = "w")

        lblFirstName = tk.Label(self,text = "First Name:")
        lblFirstName.grid(column = 0,row = 3,sticky = "e")
        entryFirstName = tk.Entry(self,width = 20,textvariable = firstName)
        entryFirstName.grid(column = 1,row = 3,sticky = "w")

        lblLastName = tk.Label(self,text = "Last Name:")
        lblLastName.grid(column = 0,row = 4,sticky = "e")
        entryLastName = tk.Entry(self,width = 20,textvariable = lastName)
        entryLastName.grid(column = 1,row = 4,sticky = "w")

        lblEmail = tk.Label(self,text = "Email:")
        lblEmail.grid(column = 0,row = 5,sticky = "e")
        entryEmail = tk.Entry(self,width = 20,textvariable = email)
        entryEmail.grid(column = 1,row = 5,sticky = "w")

        lblPhone = tk.Label(self,text = "Phone:")
        lblPhone.grid(column = 0,row = 6,sticky = "e")
        entryPhone = tk.Entry(self,width = 20,textvariable = phone)
        entryPhone.grid(column = 1,row = 6,sticky = "w")

        btnRegister = ttk.Button(self,text = "Register",
            command = lambda:register(
            '<Button-1>'
            ,parent
            ,username.get()
            ,password.get()
            ,firstName.get()
            ,lastName.get()
            ,email.get()
            ,phone.get()
            )
        )
        btnRegister.grid(column = 0,row = 7,columnspan = 2,sticky = "nsew")
