"""
    Andrew Goodman
    December 12, 2016

    A function library containing all of the
    database interaction
"""
import pymysql
from modules.database.dbconfig import dbconnect
from tkinter import *
from tkinter import messagebox


def login(event,controller,username,password):
    """Login registered users"""
    from modules.application.MainFrame import MainFrame
    db = dbconnect()

    # Validate that the username and password
    # fields are populated
    if(username == "" or username is None):
        messagebox.showwarning("Error logging in","Please enter your username")
        return -1
    elif(password == "" or password is None):
        messagebox.showwarning("Error logging in","Please enter your password")
        return -1

    # Username and Password are present
    # Validate the username/password combination
    try:
        with db.cursor() as cur:
            queryUser = """
                SELECT COUNT(username) FROM User
                WHERE username = %s AND password = %s
                """
            cur.execute(queryUser,(username,password,))
            queryResults = cur.fetchone()

            if(queryResults[0] == 1):
                # TODO: Print 'Login Successful' and load the main frame
                controller.display(MainFrame)
            else:
                # TODO: Print 'Login Failed' and erase the password field
                messagebox.showwarning("Error logging in","Please check the username or password")
    except Exception as e:
        print("DEBUG - Error logging in: {0}".format(e))
    finally:
        db.close()

def register(event,username,password,firstName,lastName,email,phone):
    """Registers a new user"""

def dbtest(event,q,t):
    """Test that the database connection works"""
    db = dbconnect()
    try:
        with db.cursor() as cur:
            query = q
            cur.execute(query)
            queryResults = cur.fetchall()
            print("database connection test: {0}".format(queryResults))
            # Insert query results to the Text widget
            t.insert(INSERT,queryResults)
            return queryResults
    except Exception as e:
        print("DEBUG - Exception occurred: {0}".format(e))
    finally:
        db.close()
