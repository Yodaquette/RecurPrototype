"""
    Andrew Goodman
    December 12, 2016

    Configure the database connection
"""
import pymysql
from modules.database.parseconfig import parseDbConnection

def dbconnect():
    """
        Create a connection to the database

        :return: database connection object
    """
    db = parseDbConnection()

    connection = pymysql.connect(
        host = db['host']
        ,user = db['user']
        ,password = db['password']
        ,database = db['database']
    )
    return connection
