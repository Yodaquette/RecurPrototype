"""
    Andrew Goodman
    December 12, 2016

    A function library containing all of the
    database interaction
"""
import pymysql
from modules.database.dbconfig import dbconnect
from tkinter import *


# Test that the database connection works
def dbtest(event,q,t):
    db = dbconnect()
    try:
        with db.cursor() as cur:
            query = q#"""SELECT * FROM User"""
            cur.execute(query)
            query_results = cur.fetchall()
            print("database connection test: {0}".format(query_results))
            t.insert(INSERT,query_results)
            return query_results
    except Exception as e:
        print("DEBUG - Exception occurred: {0}".format(e))
    finally:
        db.close()
