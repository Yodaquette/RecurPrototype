"""
    Andrew Goodman
    December 12, 2016

    Configure the database connection
"""
import pymysql

def dbconnect():
    connection = pymysql.connect(host = 'localhost'
                                ,user = 'root'
                                ,password = 'root'
                                ,db = 'recurDB'
                                ,charset = 'utf8'
                                #,cursorclass = pymysql.cursors.DictCursor
                                )
    return connection
