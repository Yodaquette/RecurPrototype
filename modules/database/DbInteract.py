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


def login(event,parent,username,password):
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
                messagebox.showinfo("Welcome","Login successful!")
                parent.display(MainFrame)
            else:
                # TODO: Print 'Login Failed' and erase the password field
                messagebox.showwarning("Error logging in","Please check the username or password")
    except Exception as e:
        print("DEBUG - Error logging in: {0}".format(e))
    finally:
        db.close()

def register(event,parent,username,password
    ,firstName = "",lastName = "",email = "",phone = "",userType = "1"
    ):
    """
        Registers a new user

        :param username: the username given by the registering user
        :param password: the password given by the registering user
        :param firstName: (optional) first name of the registering user
        :param lastName: (optional) last name of the registering user
        :param email: (optional) email address of the registering user
        :param phone: (optional) phone number of the registering user
    """
    from modules.application.MainFrame import MainFrame

    # Validate the required registration parameters
    if(username == "" or username is None):
        messagebox.showwarning("Error Registering","Username cannot be blank")
        return -1
    elif(username != "" or username is not None):
        # Check that username is not already in use
        db = dbconnect()
        with db.cursor() as cur:
            checkUsername = """
                SELECT COUNT(username)
                FROM User WHERE username = %s
                """
            cur.execute(checkUsername,(username,))
            checkUsernameResult = cur.fetchone()
            if(checkUsernameResult[0] == 1):
                messagebox.showwarning("Error Registering","Username already in use")
                return -1
    if(password == "" or password is None):
        messagebox.showwarning("Error Registering","Password cannot be blank")
        return -1

    # Required registration info is present
    # and the info has been validated
    try:
        db = dbconnect()
        with db.cursor() as cur:
            # Insert user into the database
            registerUser = """
                INSERT INTO
                    User (userTypeID_FK,username,password,firstName,lastName,email,phone)
                VALUES
                    (%s,%s,%s,%s,%s,%s,%s)
                """
            cur.execute(registerUser,(userType,username,password,firstName,lastName,email,phone,))

            # Check that the insert was successful
            checkUser = """
                SELECT COUNT(username)
                FROM User WHERE username = %s
                """
            cur.execute(checkUser,(username,))
            checkUserResult = cur.fetchone()
            if(checkUserResult[0] == 1):
                # TODO: Print 'Registration Successful' and load the main frame
                messagebox.showinfo("Registration Successful","Welcome to the Recur App Prototype")
                parent.display(MainFrame)
            else:
                raise Exception("Error occurred during registration")
    except Exception as e:
        print("DEBUG - Error occurred during registration {0}".format(str(e)))
    finally:
        db.commit()
        db.close()


# def dbtest(event,q,t):
#     """
#         Validate that the database connection works
#
#         :param event: tkinter event initiated by the user
#         :param q: user database query
#         :param t: tkinter text widget
#     """
    # db = dbconnect()
    # try:
    #     with db.cursor() as cur:
    #         query = q
    #         cur.execute(query)
    #         queryResults = cur.fetchall()
    #         print("database connection test: {0}".format(queryResults))
    #         # Insert query results to the Text widget
    #         t.insert(INSERT,queryResults)
    #         return queryResults
    # except Exception as e:
    #     print("DEBUG - Exception occurred: {0}".format(e))
    # finally:
    #     db.close()
