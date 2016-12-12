"""
    --Authors--
    Morgan Mitchell
    Andrew Goodman

    --Date--
    December 12, 2016

    UI for the recur prototype
"""
from tkinter import *
import pymysql
from modules.system.SystemData import SystemData
from modules.database.dbconfig import dbconnect

db = dbconnect()

print("database: {0}".format(db))
