"""
    --Authors--
    Morgan Mitchell
    Andrew Goodman

    --Date--
    December 12, 2016

    Recur application prototype
"""
from tkinter import *
import pymysql
from modules.system.SystemData import SystemData
from modules.database.dbconfig import dbconnect

# Connect to the database
db = dbconnect()

# Test that the database connection works
# def dbtest():
#     try:
#         with db.cursor() as cur:
#             query = """SELECT * FROM User"""
#             cur.execute(query)
#             query_results = cur.fetchall()
#             print("database connection test: {0}".format(query_results))
#     except Exception as e:
#         print("DEBUG - Exception occurred: {0}".format(e))
#     finally:
#         db.close()
#
# dbtest()
